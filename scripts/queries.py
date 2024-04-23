import os
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv

def get_engine():
    """Configuracion del motor de base de datos para PostgreSQL"""
    load_dotenv()
    username = os.getenv('DB_USERNAME')
    password = os.getenv('DB_PASSWORD')
    host = os.getenv('DB_HOST')
    port = os.getenv('DB_PORT')
    database = os.getenv('DB_DATABASE')
    engine = create_engine(f"postgresql+psycopg2://{username}:{password}@{host}:{port}/{database}")
    return engine

dataset = pd.read_csv("data/electronic-card-transactions-october-2023-csv-tables-clean.csv")
dataset.to_sql(name='transaction', if_exists='replace', con=get_engine(), index=False)

def cargar():
    """Imprime en pantalla todas las transacciones"""
    sql_df = pd.read_sql("SELECT * FROM transaction", con=get_engine())
    print(sql_df)

def cargar_50():
    """Imprime en pantalla las primeras 50 transacciones con todos sus datos"""
    sql_df = pd.read_sql("SELECT * FROM transaction LIMIT 50", con=get_engine())
    print(sql_df)
