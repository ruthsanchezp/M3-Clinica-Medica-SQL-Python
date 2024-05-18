import psycopg2

 # Configurar la conexión a la base de datos
def connect_db():
    return psycopg2.connect(
        dbname='',
        user='postgres',
        password='',
        host='localhost',
    )
