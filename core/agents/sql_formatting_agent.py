import os 
import logging 
from openai import OpenAI

client = OpenAI()

def format_sql_step(schema_text):
    sql_format_agent = client.chat.completions.create(
        temperature = 0.4,
        model = 'chatgpt-4o-latest',
        messages = [
            {
                "role": "developer", 
                "content":
                    """
                        You are a helpful custom SQL formatting assistant:

                        Prioritize left-hand side, before column-name, commas. This is a must! 
                        Prioritize ALL CAPS for SQL statements. 
                        Prioritize using correct syntax for data types, if a user provides a wrong data type adjust. 
                        IE if bigint is provided, but snowflake datawarehouse only understands NUMBERS;
                        Please just output the stylized SQL. No markdown please

                        Including all of the above prioritizations, include SQL rivers 
                            and don't wrap SQL lines if less than 250 chars. 

                        For any edge-cases, follow ANSII SQL style guides.
                        Nothing else may be output that isn't SQL text (no emojis please)
                    """
            }, 
            {
                "role": "user", 
                "content": schema_text
            }

        ]
    )

    formatted_sql = sql_format_agent.choices[0].message.content
    return formatted_sql

if __name__=="__main__":
    format_sql_step

# print(sql_format_agent.choices[0].message.content)