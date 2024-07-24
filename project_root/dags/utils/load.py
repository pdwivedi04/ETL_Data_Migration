import pandas as pd # type: ignore
import snowflake.connector # type: ignore
from snowflake.connector.pandas_tools import write_pandas # type: ignore
from config import SNOWFLAKE_CONN

def load_data(activity_data):
    conn = snowflake.connector.connect(
        user=SNOWFLAKE_CONN['user'],
        password=SNOWFLAKE_CONN['password'],
        account=SNOWFLAKE_CONN['account'],
        warehouse=SNOWFLAKE_CONN['warehouse'],
        database=SNOWFLAKE_CONN['database'],
        schema=SNOWFLAKE_CONN['schema']
    )
    write_pandas(conn, activity_data, 'activity_assignment_archive')
    conn.close()
