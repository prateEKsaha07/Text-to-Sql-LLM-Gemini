def get_prompt(user_input, schema):
    return f"""
You are an expert SQL generator.

Database Schema:
{schema}

Rules:
- Only return SQL
- Use SQLite syntax
- If not possible, return: I DON'T KNOW

User Question:
{user_input}"""

def fix_sql_prompt(user_input,schema,bad_query,error):
    return f"""
    You are an expert SQL generator.

    Convert the following natural language into a valid SQLite query.
    
    Database Schema:
    {schema}

    User Question:
    {user_input}

    previous SQL Query:
    {bad_query}

    error:
    {error}

    Rules:
    - Only return SQL query
    - Do NOT explain anything
    - Use SQLite syntax
    - Table name: students
    - Columns: id, name, age, marks 
"""