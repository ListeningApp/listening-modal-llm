"""
Example usage:
    # Export TSV files to the Downloads folder
    poetry run python src/clean.py --outdir ~/Downloads
"""

import csv
import json
import os
import re
from typing import NamedTuple

MISSING_VALUE_KEY = '<| MISSING |>'
REGEX_FILENAME_PAGE_SECTION = re.compile(r'^[a-z_\.]+_p(\d+)_s(\d+)[a-z_\.]+$')


class CsvRowLabel(NamedTuple):
    docname: str
    textbox_id: str
    label: str
    text: str


class PageSection(NamedTuple):
    page: int
    section: int

    @staticmethod
    def from_filename(filename: str) -> 'PageSection':
        matches = REGEX_FILENAME_PAGE_SECTION.match(filename)
        page_str = matches.group(1)  # type: ignore [union-attr]
        section_str = matches.group(2)  # type: ignore [union-attr]
        return PageSection(int(page_str), int(section_str))


def export_csv(outdir: str) -> None:  # noqa: C901
    # Open output TSV files, one for labels and one for updates
    with (
        open(f'{outdir}/labels.tsv', 'w', newline='') as labels_tsv,
        open(f'{outdir}/updates.tsv', 'w', newline='') as updates_tsv,
    ):
        # Initialize TSV writers
        labels_tsv_writer = csv.writer(labels_tsv, delimiter='\t')
        updates_tsv_writer = csv.writer(updates_tsv, delimiter='\t')

        # Write heading rows
        labels_tsv_writer.writerow(['Document', 'Textbox ID', 'Label', 'Text'])
        updates_tsv_writer.writerow(['Document', 'Textbox ID', 'Original', 'Updated'])

        # Iterate each directory in the training documents folder
        for dirname in os.listdir('training_documents'):
            label_prompt_filenames: list[str] = []
            update_prompt_filenames: list[str] = []

            # Skip non-cache directories
            if not dirname.endswith('_cache') or not os.path.isdir(f'training_documents/{dirname}'):
                continue

            # Get the prefix name of this directory (strip the '_cache' suffix)
            docname = dirname[:-6]

            # Get all the prompt files in this directory of each type
            for filename in os.listdir(f'training_documents/{dirname}'):
                if not filename.endswith('.prompt.txt'):
                    continue
                if filename.startswith(f'{docname}.llm.label'):
                    label_prompt_filenames.append(filename)
                elif filename.startswith(f'{docname}.llm.update'):
                    update_prompt_filenames.append(filename)

            # Sort files by page, then by section
            label_prompt_filenames.sort(key=PageSection.from_filename)
            update_prompt_filenames.sort(key=PageSection.from_filename)

            # Read each label prompt file in order
            for label_filename in label_prompt_filenames:
                label_completion_filename = label_filename.replace('.prompt.txt', '.json')

                # Open the input prompt file and the output completion file
                with (
                    open(f'training_documents/{dirname}/{label_filename}') as prompt_file,
                    open(f'training_documents/{dirname}/{label_completion_filename}') as completion_file,
                ):
                    # Load completions
                    label_completion_file_dict = json.load(completion_file)
                    label_completion = label_completion_file_dict['choices'][0]['message']['content']
                    label_completion_dict: dict[str, str] = {}

                    # Build the dict of completions by ID
                    for ln in label_completion.split('\n'):
                        tid, _, label = ln.partition('|')
                        tid = tid.strip()
                        label = label.strip()
                        if tid:
                            label_completion_dict[tid] = label

                    # Load the prompt, skipping the instruction part
                    prompt = prompt_file.read()
                    prompt_start_idx = prompt.index('\n\n\n') + 3
                    prompt = prompt[prompt_start_idx:].strip()

                    # Write each row from the prompt to the TSV
                    for line in prompt.split('\n'):
                        tid, _, text = line.partition('|')
                        tid = tid.strip()
                        text = text.strip()

                        if tid and text:
                            label = label_completion_dict.get(tid, MISSING_VALUE_KEY)
                            labels_tsv_writer.writerow([docname, tid, label, text])

            # Read each update prompt file in order
            for update_filename in update_prompt_filenames:
                update_completion_filename = update_filename.replace('.prompt.txt', '.json')

                # Open the input prompt file and the output completion file
                with (
                    open(f'training_documents/{dirname}/{update_filename}') as prompt_file,
                    open(f'training_documents/{dirname}/{update_completion_filename}') as completion_file,
                ):
                    # Load completions
                    update_completion_file_dict = json.load(completion_file)
                    update_completion = update_completion_file_dict['choices'][0]['message']['content']
                    update_completion_dict: dict[str, str] = {}

                    # Build the dict of completions by ID
                    for ln in update_completion.split('\n'):
                        tid, _, update = ln.partition('|')
                        tid = tid.strip()
                        update = update.strip()
                        if tid:
                            update_completion_dict[tid] = update

                    # Load the prompt, skipping the instruction part
                    prompt = prompt_file.read()
                    prompt_start_idx = prompt.index('\n\n\n') + 3
                    prompt = prompt[prompt_start_idx:].strip()

                    # Write each row from the prompt to the TSV
                    for line in prompt.split('\n'):
                        tid, _, text = line.partition('|')
                        tid = tid.strip()
                        text = text.strip()

                        if tid and text:
                            update = update_completion_dict.get(tid, MISSING_VALUE_KEY)
                            updates_tsv_writer.writerow([docname, tid, text, update])


def import_csv(infile: str) -> None:
    pass


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('-o', '--outdir')
    parser.add_argument('-i', '--infile')
    args = parser.parse_args()

    if args.outdir:
        export_csv(args.outdir)
    elif args.infile:
        import_csv(args.infile)
