import os 
import logging 
from core.agents import *

logging.basicConfig(level=logging.INFO)


def build(file_name, schema_text, step):
    """
    Build
    -----

    Determines the SQL statement step based on input. It should always do the create table step 
    first, then run the insert into statement
    """

    if step == 'create_table':
        create_table = create_table_step(schema_text)
        create_table = format_sql_step(create_table)
        with open(file_name, 'w') as fname:
            fname.writelines(create_table)

    elif step == 'insert_into':
        insert_data = insert_step(schema_text) # uses schema text to actually use the 
        insert_data = format_sql_step(insert_data)
        with open(file_name, 'w') as fname:
            fname.writelines(insert_data)
    else:
        pass

# ADD SCHEMA COLUMN NAMES AND DATA TYPES HERE: 
schema_text = """

"""

create_table_file = 'create_table.sql'
insert_into_file = 'insert_into.sql'

build(
    file_name=create_table_file,
    schema_text=schema_text,
    step='create_table'
)

build(
    file_name=insert_into_file,
    schema_text=schema_text,
    step='insert_into'
)