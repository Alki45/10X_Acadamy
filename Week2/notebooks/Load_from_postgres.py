import pandas as pd
from sqlalchemy import create_engine

def load_data():
    # Database connection parameters
    db_user = 'alki'
    db_password = 'alki'
    db_host = 'localhost'
    db_port = '5432'
    db_name = 'telecom_db'

    # Create a SQLAlchemy engine
    engine = create_engine(f'postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}')

    # Query to execute
    query = 'SELECT * FROM public.xdr_data;'

    try:
        # Load data into DataFrame
        loading_data = pd.read_sql(query, engine)
        return loading_data
    except Exception as e:
        print(f"Error loading data: {e}")
        return None