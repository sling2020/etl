import logging as log
import pandas as pd
from sqlalchemy import create_engine

# Crear una conexión a SQLite
engine = create_engine('sqlite:///my_database.db')

# Suponiendo que tienes un DataFrame llamado 'df'
df = pd.DataFrame({'id': [1, 2], 'name': ['Alice', 'Bob'], 'age': [25, 30]})

# Definir los tipos de datos al cargar en la base de datos
dtype = {
    'id': 'INTEGER',
    'name': 'TEXT',
    'age': 'INTEGER'
}

# Cargar el DataFrame en una tabla llamada 'users', especificando los tipos de datos
df.to_sql('users', con=engine, if_exists='replace', index=False, dtype=dtype)
