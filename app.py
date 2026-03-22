import streamlit as st
from llm import generate_sql
from create_prompt import get_prompt
from db import run_query, get_schema
import pandas as pd
from create_prompt import fix_sql_prompt

if "messages" not in st.session_state:
    st.session_state.messages = []

schema = get_schema()

st.title("Text to SQL using Groq (LLaMA 3)")

# user_input = st.text_input("Enter your question:")

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])


user_input = st.chat_input("ask your database...")


if user_input:
    st.session_state.messages.append({"role":"user","content":user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    #query generation
    prompt = get_prompt(user_input,schema)
    sql_query = generate_sql(prompt)

    #show assistant message
    with st.chat_message("assistant"):
        st.code(sql_query,language='sql')

        if "I DON'T KNOW" in sql_query:
            st.warning("query not related to data base..")
        
        else:
            rows,cols,errors = run_query(sql_query)

            # retry logic
            if errors:
                fix_prompt = fix_sql_prompt(user_input,schema,sql_query,errors)
                fixed_sql = generate_sql(fix_prompt)

                st.code(fixed_sql,language="sql")
                rows,cols,errors = run_query(fixed_sql)
            if errors:
                st.error(errors)
            else:
                if rows:
                    df = pd.DataFrame(rows,columns=cols)
                    st.dataframe(df)
                    if len(df.columns) == 2:
                        st.bar_chart(df.set_index(df.columns[0]))
                else:
                    st.warning("no results found")
    # save responses
    st.session_state.messages.append({
        "role":"assistant",
        "content" : f"```sql\n{sql_query}\n```"
    })


# old v2

# if st.button("Generate"):
#     prompt = get_prompt(user_input, schema)
#     sql_query = generate_sql(prompt)
#     st.code(sql_query, language="sql")

#     if "I DON'T KNOW" in sql_query:
#         st.warning("Query not related to database") 
    

#     else:
#         rows, cols, error = run_query(sql_query)

#         if error:
#             st.warning("Query failed, trying to fix...")
#             fix_prompt = fix_sql_prompt(user_input, schema, sql_query, error)
#             fixed_sql = generate_sql(fix_prompt)

#             st.code(fixed_sql, language="sql")


#             rows, cols, error = run_query(fixed_sql)
#         if error:
#             st.error(error)
#         else:
#             if not rows:
#                 st.warning("No results found")
#             else:
#                 df = pd.DataFrame(rows, columns=cols)
#                 st.dataframe(df)

# old v1 
        # rows, cols = run_query(sql_query)
        # if isinstance(rows, str):
        #     st.error(rows)

        # else:
        #     if not rows:
        #         st.warning("No results found")

        #     else:
        #         df = pd.DataFrame(rows, columns=cols)
        #         st.dataframe(df)