import pdb
import duckdb
import streamlit as st


answer_string = """
SELECT * FROM beverages
CROSS JOIN food_items
"""

solution_df = duckdb.sql(answer_string).df()


with st.sidebar:
    option = st.selectbox(
        "What would you like to review?",
        ("Joins", "GroupBy", "Windows Functions"),
        index=None,
        placeholder="Select a theme...",
    )
    st.write("You selected:", option)


st.header("enter your code:")
query = st.text_area(label="votre code SQL ici", key="user_input")
if query:
    result = duckdb.sql(query).df()
    try:
        result = result[solution_df.columns]
        st.dataframe(result.compare(solution_df))

    except:
        st.write("some columns are missing")

    st.dataframe(result)


tab2, tab3 = st.tabs(["Tables", "solution_df"])

with tab2:
    st.write("table: beverages")
    st.dataframe(beverages)
    st.write("table: food_items")
    st.dataframe(food_items)
    st.write("expected:")
    st.dataframe(solution_df)

with tab3:
    st.write(answer_string)
