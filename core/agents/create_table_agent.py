import os 
import logging 
from openai import OpenAI


client = OpenAI()

def create_table_step(schema_text):


    agent = client.chat.completions.create(
        model = 'chatgpt-4o-latest',
        messages = [
            {
                "role": "developer", 
                "content":
                    """
                        You are a helpful assistant that writes CREATE TABLE DML statements

                        Your output should be as contextually relevant to the columns and data-types as possible.
                        Prioritize using correct syntax for data types, if a user provides a wrong data type adjust. 
                        IE if bigint is provided, but snowflake datawarehouse only understands NUMBERS;
                        Please just output the stylized SQL. No markdown please
                    """
            }, 
            {
                "role": "user", 
                "content": schema_text
            }
        ]
    )

    create_table_sql = agent.choices[0].message.content
    return create_table_sql

if __name__=="__main__":
    # print(create_table_sql)
    create_table_step