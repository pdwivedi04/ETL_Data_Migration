from sqlalchemy import create_engine # type: ignore
import pandas as pd # type: ignore
from config import POSTGRES_CONN

def extract_data():
    engine = create_engine(f"postgresql+psycopg2://{POSTGRES_CONN['user']}:{POSTGRES_CONN['password']}@{POSTGRES_CONN['host']}:{POSTGRES_CONN['port']}/{POSTGRES_CONN['database']}")
    query = "SELECT * FROM master_config.Activity_assignment"
    activity_data = pd.read_sql(query, engine)
    return activity_data
