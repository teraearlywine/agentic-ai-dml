"""

python -m core.format some_file.sql
"""
import os 
from core.agents import *
import argparse


def sql(file_name):
    """
    Formats SQL by reading then re-writing the text to the same file
    """
    file_path = f'SQL/{file_name}'

    with open(file_path, 'r') as file:
        sql_text = file.read()
        formatted_sql = format_sql_step(schema_text=sql_text)  # Formats any sort of text string


    with open(f'SQL/{file_name}', 'w') as fname:
        fname.writelines(formatted_sql)


def main():
    parser = argparse.ArgumentParser(description='Format a SQL file.')
    parser.add_argument('file_name', type=str, help='The name of the SQL file to format')
    args = parser.parse_args()

    sql(args.file_name)

if __name__ == '__main__':
    main()