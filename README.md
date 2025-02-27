# AI DML

## Summary
This repository helps you write and format SQL. Actually, it enables proactive data model design and development in situations where real data is not available. The models can work with and extract the appropriate information to build your SQL.

The SQL built:
1. **CREATE TABLE** → The agent that supports this step makes inferences based on the column name and data type.
2. **INSERT INTO / VALUES** → The agent that supports this step generates synthetic data to enable proactive data modeling based on the description of the columns.

## Security & Privacy Concerns

**PLEASE READ BEFORE YOU GET STARTED**

1. As with any AI or LLM prompt-engineering, be mindful of the context of your data. Especially if it’s a non-sanctioned tool, do not provide sensitive or confidential information.
2. Often in data modeling, there is a human element—like a user, patient, or employee. Health care, financial, and banking info are included here too. Under no circumstances is specific record information recommended to be passed to the prompt. This is about generating pertinent *fake* data to avoid potential PII/security mishaps. It’s not a crime to pass a schema because it shares no real data context. Remember: all generated data is fictional (and may be a hilarious misrepresentation of reality).

> **Note**: A schema is the complete list of columns that form the structure of a database table. We’re providing these names, descriptions, and data types to the LLM—no real data needed.

## Prompt Engineering as an Alternative

If you want highly tailored synthetic data that follows best practices in data modeling, you can go the route of detailed prompt engineering. For instance: