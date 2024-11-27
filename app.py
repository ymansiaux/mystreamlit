import streamlit as st
import pandas as pd
import duckdb
import io

data = {"a": [1, 2, 3], "b": [4, 5, 6]}
df = pd.DataFrame(data)

st.write("App pour faire du SQL")
# ------------------------------------------------------------
# CROSS JOIN EXERCISES
# ------------------------------------------------------------
csv = """
beverage,price
orange juice,2.5
Expresso,2
Tea,3
"""
beverages = pd.read_csv(io.StringIO(csv))

csv2 = """
food_item,food_price
cookie juice,2.5
chocolatine,2
muffin,3
"""
food_items = pd.read_csv(io.StringIO(csv2))


sizes = """
size
XS
M
L
XL
"""
sizes = pd.read_csv(io.StringIO(sizes))


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
