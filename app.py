import streamlit as st
import pandas as pd
import duckdb

data = {"a": [1, 2, 3], "b": [4, 5, 6]}
df = pd.DataFrame(data)

st.write("App pour faire du SQL")

with st.sidebar:
    option = st.selectbox(
        "What would you like to review?",
        ("Joins", "Group by", "Windows functions"),
        index=None,
        placeholder="Select something...",
    )

    st.write("You selected:", option)

    input_text = st.text_area("Please enter your sql")
    st.dataframe(df)

st.write("resultat")
duckres = duckdb.query(input_text)
st.dataframe(duckres)
