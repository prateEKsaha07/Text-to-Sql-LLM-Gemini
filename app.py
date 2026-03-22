import streamlit as st
from llm import generate_sql
from create_prompt import get_prompt
from db import run_query
import pandas as pd

st.title("text to sql queries LLM using Groq LLama - 3.3.106")
user_input = st.text_input("enter your question:")

if st.button("generate"):
    prompt = get_prompt(user_input)

    sql_query = generate_sql(prompt)
    st.code(sql_query,language="sql")

    result = run_query(sql_query)

    df = pd.DataFrame(result)
    st.dataframe(df)

    st.write("### Results:")
    st.write([row[0] for row in result])