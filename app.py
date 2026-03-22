import streamlit as st
from llm import generate_sql
from create_prompt import get_prompt
from db import run_query, get_schema
import pandas as pd

schema = get_schema()

st.title("Text to SQL using Groq (LLaMA 3)")

user_input = st.text_input("Enter your question:")

if st.button("Generate"):
    prompt = get_prompt(user_input, schema)
    sql_query = generate_sql(prompt)
    st.code(sql_query, language="sql")

    if "I DON'T KNOW" in sql_query: # type: ignore
        st.warning("Query not related to database") 
    else:
        rows, cols = run_query(sql_query)
        if isinstance(rows, str):
            st.error(rows)

        else:
            if not rows:
                st.warning("No results found")

            else:
                df = pd.DataFrame(rows, columns=cols)
                st.dataframe(df)