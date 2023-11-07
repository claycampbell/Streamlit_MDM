import snowflake.connector

def get_snowflake_connection():
    conn_params = {
        'user': '',
        'password': '',
        'account': '',
        'warehouse': '',
        'database': '',
        'schema': ''
    }
    # Create a connection
    ctx = snowflake.connector.connect(
        user=conn_params['user'],
        password=conn_params['password'],
        account=conn_params['account'],
        warehouse=conn_params['warehouse'],
        database=conn_params['database'],
        schema=conn_params['schema']
    )
    return ctx
