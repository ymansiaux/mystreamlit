import pdb
import ast
import duckdb
import streamlit as st

con = duckdb.connect(database="data/exercices_sql_tables.duckdb", read_only=False)


# answer_string = """
# SELECT * FROM beverages
# CROSS JOIN food_items
# """

# solution_df = duckdb.sql(answer_string).df()


with st.sidebar:
    theme = st.selectbox(
        "What would you like to review?",
        ("cross_joins", "GroupBy", "windows_functions"),
        index=None,
        placeholder="Select a theme...",
    )
    st.write("You selected:", theme)
    if theme:
        exercise = (
            con.execute(f"SELECT * FROM memory_state WHERE theme = '{theme}'")
            .df()
            .sort_values("last_reviewed", ascending=False)
            .reset_index(drop=True)
        )
        st.write(exercise)

        exercise_name = exercise.loc[0, "exercise_name"]
        with open(f"answers/{exercise_name}.sql") as f:
            answer = f.read()
        solution_df = con.execute(answer).df()

st.header("enter your code:")
query = st.text_area(label="votre code SQL ici", key="user_input")
if query:
    result = con.execute(query).df()

    try:
        result = result[solution_df.columns]
        st.dataframe(result.compare(solution_df))

    except:
        st.write("some columns are missing")

    st.dataframe(result)


tab2, tab3 = st.tabs(["Tables", "solution_df"])

with tab2:
    if theme:
        exercise_tables = exercise.loc[
            0, "tables"
        ]  # en fait on obtient une str au lieu d'une liste, on va lui demander de le lire "literally"
        # exercise_tables = ast.literal_eval(exercise_tables)

        for table in exercise_tables:
            st.write(f"table: {table}")
            table_df = con.execute(f"SELECT * FROM {table}").df()
            st.dataframe(table_df)

with tab3:
    if theme:
        st.write(answer)

con.close()
