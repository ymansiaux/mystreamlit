import duckdb

con = duckdb.connect(database="data/exercices_sql_tables.duckdb", read_only=False)
test = con.execute("SELECT * FROM beverages CROSS JOIN food_items").df()
print(test)


test = con.execute("SELECT * FROM memory_state").df()
print(test)
