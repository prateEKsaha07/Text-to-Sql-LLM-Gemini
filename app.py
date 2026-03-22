import streamlit as st
from llm import generate_sql
from create_prompt import get_prompt
from db import run_query, get_schema
import pandas as pd
from create_prompt import fix_sql_prompt

schema = get_schema()

st.title("Text to SQL using Groq (LLaMA 3)")

user_input = st.text_input("Enter your question:")

if st.button("Generate"):
    prompt = get_prompt(user_input, schema)
    sql_query = generate_sql(prompt)
    st.code(sql_query, language="sql")

    if "I DON'T KNOW" in sql_query:
        st.warning("Query not related to database") 
    

    else:
        rows, cols, error = run_query(sql_query)

        if error:
            st.warning("Query failed, trying to fix...")
            fix_prompt = fix_sql_prompt(user_input, schema, sql_query, error)
            fixed_sql = generate_sql(fix_prompt)

            st.code(fixed_sql, language="sql")


            rows, cols, error = run_query(fixed_sql)
        if error:
            st.error(error)
        else:
            if not rows:
                st.warning("No results found")
            else:
                df = pd.DataFrame(rows, columns=cols)
                st.dataframe(df)
                
        # rows, cols = run_query(sql_query)
        # if isinstance(rows, str):
        #     st.error(rows)

        # else:
        #     if not rows:
        #         st.warning("No results found")

        #     else:
        #         df = pd.DataFrame(rows, columns=cols)
        #         st.dataframe(df)