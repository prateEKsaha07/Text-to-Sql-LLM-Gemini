import sqlite3

def connect_db():
    return sqlite3.connect("database.db")

def run_query(query):
    conn = connect_db()
    cursor = conn.cursor()

    try: 
        cursor.execute(query)
        rows = cursor.fetchall()
        return rows 
    except Exception as e:
        return str(e)
    finally:
        cursor.close()