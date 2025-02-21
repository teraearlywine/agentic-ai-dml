import os 
import logging 
from openai import OpenAI


client = OpenAI()

def mermaid_erd_step(text):


    agent = client.chat.completions.create(
        model = 'chatgpt-4o-latest',
        messages = [
            {
                "role": "developer", 
                "content":
                    """
                    You are a helpful and super smart assistant that loves to create mermaid entity relationship diagrams
                    If there is no discernable pattern, just do your best to parse the information
                        1. Parse the input text and extract table names, columns, and their data types.
                        2. For each table, list every column alongside its data type.
                        3. If a column appears in more than one table, ensure it’s included in each table definition.
                        4. Optionally, infer relationships between tables based on common patterns (e.g., columns named like "user_id" suggest a foreign key relationship).
                        5. Output the entire diagram using valid Mermaid syntax.
                        6. Skip markdown, no extra ```mermaid or words please.

                    Example Input:
                    "Table: Customers
                    - id: int
                    - name: varchar
                    - email: varchar

                    Table: Orders
                    - id: int
                    - order_date: datetime
                    - customer_id: int"

                    Expected Output:

                    erDiagram
                        CUSTOMERS {
                            int id
                            varchar name
                            varchar email
                        }
                        ORDERS {
                            int id
                            datetime order_date
                            int customer_id
                        }
                        CUSTOMERS ||--o{ ORDERS : "has orders"

                    """
            }, 
            {
                "role": "user", 
                "content": text
            }
        ]
    )

    output = agent.choices[0].message.content
    return output

if __name__=="__main__":
    # print(create_table_sql)
    mermaid_erd_step