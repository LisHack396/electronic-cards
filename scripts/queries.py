import pandas as pd
from sqlalchemy import create_engine

def get_engine():
    """Configuracion del motor de base de datos para PostgreSQL"""
    username = "postgres"
    password = "anubKnsV"
    host = "127.0.0.1"
    port = "5432"
    engine = create_engine(f"postgresql+psycopg2://{username}:{password}@{host}:{port}/electronic_cards")
    return engine

dataset = pd.read_csv("data/electronic-card-transactions-october-2023-csv-tables-clean.csv")
dataset.to_sql(name='transaction', if_exists='replace', con=get_engine(), index=False)


def cargar():
    """Imprime en pantalla las primeras 50 transacciones con todos sus datos"""
    sql_df = pd.read_sql("SELECT * FROM transaction LIMIT 50", con=get_engine())
    print(sql_df)
