from openai import OpenAI
import os
from dotenv import load_dotenv

print(os.getenv("GROQ_API_KEY"))

load_dotenv()

client= OpenAI(
    api_key = os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)

def generate_sql(prompt):
    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
            {"role": "system", "content": "You are an expert SQL generator. Only return SQL queries."},
            {"role": "user", "content": prompt}
        ]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error: {str(e)}"