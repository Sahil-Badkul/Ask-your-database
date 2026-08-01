import psycopg

def execute_query(query, params=None):
    """
    Executes a SQL query against the PostgreSQL database.

    :param query: The SQL query to execute.
    :param params: Optional parameters for the SQL query.
    :return: The result of the query execution.
    """
    try:
        # Establish a connection to the PostgreSQL database
        with psycopg.connect(
            host="localhost",
            port=5432,
            dbname ="postgres",
            user="mayankjain"
        ) as conn:
            with conn.cursor() as cur:
                # Execute the query with optional parameters
                cur.execute(query, params)
                
                # If it's a SELECT query, fetch and return the results
                if query.strip().upper().startswith("SELECT"):
                    rows = cur.fetchall()
                    columns = [desc[0] for desc in cur.description] if cur.description else []
                    return rows, columns
                else:
                    # For INSERT/UPDATE/DELETE queries, commit the changes
                    conn.commit()
                    return cur.rowcount  # Return the number of affected rows
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def get_schema(table_name):
    query = f"""SELECT column_name, data_type
        FROM information_schema.columns
        WHERE 
            table_schema = 'public'
            AND table_name = '{table_name}'"""
    result = execute_query(query)
    if not result:
        return ""

    rows, columns = result
    return "\n".join([f"{column}: {data_type}" for column, data_type in rows])


# result = execute_query("SELECT * FROM orders limit 10")
# print(result)