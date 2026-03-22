import sqlite3

def connect_db():
    return sqlite3.connect("database.db")

def run_query(query):
    conn = connect_db()
    cursor = conn.cursor()
    
    try:
        cursor.execute(query)
        rows = cursor.fetchall()
        columns = [desc[0] for desc in cursor.description]
        return rows, columns
    except Exception as e:
        return str(e), None
    finally:
        conn.close()

def get_schema():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()

    schema = ""

    for table in tables:
        table_name = table[0]
        cursor.execute(f"PRAGMA table_info({table_name});")
        columns = cursor.fetchall()

        schema += f"\n table: {table_name}"
        for column in columns:
            schema += f"- {column[1]}({column[2]})\n"

    conn.close()
    return schema

