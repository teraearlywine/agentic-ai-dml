import os 
import logging 
from openai import OpenAI

client = OpenAI()

def insert_step(schema_text):
    insert_into_agent = client.chat.completions.create(
        model = 'chatgpt-4o-latest',
        messages = [
            {
                "role": "developer", 
                "content":
                    """
                        You are a helpful assistant that writes INSERT INTO DML statements 
                        and gets to generate fake data for the VALUES part! 

                        Your output should be as contextually relevant to the entity as possible.
                        Generate 25-30 records. No markdown please
                    """
            }, 
            {
                "role": "user", 
                "content": schema_text
            }
        ]
    )

    insert_into_sql = insert_into_agent.choices[0].message.content
    return insert_into_sql

if __name__=="__main__":
    # print(insert_into_sql)
    insert_step