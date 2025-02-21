import os 
import logging 
from agents import *

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


schema_text = """
connector table: stages			connector table: application_stages	
Column Name	Data Type		Column Name	Data Type
id	bigint		application_id	bigint
organization_id	bigint		stage_id	bigint
name	character varying(1024)		entered_on	timestamp
order	integer		exited_on	timestamp
active	boolean		stage_name	character varying
created_at	timestamp		organization_id	bigint
updated_at	timestamp			

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