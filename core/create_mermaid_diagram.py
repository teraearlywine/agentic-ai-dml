"""
Use format_sql_step(some_text) to format any sql file 

`python -m core.create_mermaid_diagram bic.txt`
"""
import os 
from core.agents import *
import argparse


def create_diagram(file_name):
    """
    Formats SQL by reading then re-writing the text to the same file
    """
    file_path = f'diagrams/{file_name}'

    with open(file_path, 'r') as file:
        text = file.read()
        mermaid_diagram = mermaid_erd_step(text=text)  # Formats any sort of text string

    if file_name.endswith('.txt'):
        file_name = file_name[:-4] + '.md'

    with open(f'diagrams/{file_name}', 'w') as fname:
        fname.writelines(mermaid_diagram)


def main():
    parser = argparse.ArgumentParser(description='Create a mermaid file.')
    parser.add_argument('file_name', type=str, help='The name of the mermaid file to format')
    args = parser.parse_args()

    create_diagram(args.file_name)

if __name__ == '__main__':
    main()