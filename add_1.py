from snowflake.snowpark.functions import col

def add_one_to_column(session, table_name, column_name):
    df = session.table(table_name)
    updated_df = df.withColumn(column_name, col(column_name) + 1)
    return updated_df
