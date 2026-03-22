def get_prompt(user_input):
    return f"""
    You are an expert SQL generator.

    Convert the following natural language into a valid SQLite query.

    Rules:
    - Only return SQL query
    - Do NOT explain anything
    - Use SQLite syntax
    - Table name: students
    - Columns: id, name, age, marks 
    User Question:
    {user_input}
    """