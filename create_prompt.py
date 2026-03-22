def get_prompt(user_input,schema):
    return f"""
    You are an expert SQL generator.

    Convert the following natural language into a valid SQLite query.
    
    Database Schema:
    {schema}

    Rules:
    - Only return SQL query
    - Do NOT explain anything
    - Use SQLite syntax
    - Table name: students
    - Columns: id, name, age, marks 
    User Question:
    {user_input}
    """