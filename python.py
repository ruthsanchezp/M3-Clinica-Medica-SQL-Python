import psycopg2
from psycopg2 import Error

# Configura los parámetros de conexión
conexion_parametros = {
    "host": "host",
    "database": "database",
    "user": "user",
    "password": "pass"
}

# Sentencias SQL para crear las tablas
sentencias_sql = [
    """CREATE TABLE Habitacion (
        id_habitacion SERIAL PRIMARY KEY,
        numero_habitacion INT
    )""",
    """CREATE TABLE Cama (
        id_cama SERIAL PRIMARY KEY,
        numero_cama INT,
        id_habitacion INT,
        FOREIGN KEY (id_habitacion) REFERENCES Habitacion(id_habitacion)
    )""",
    """CREATE TABLE Paciente (
        id_paciente SERIAL PRIMARY KEY,
        nombre_paciente VARCHAR(255),
        rut VARCHAR(255) UNIQUE,
        fecha_ingreso DATE,
        fecha_alta DATE,
        id_cama INT,
        FOREIGN KEY (id_cama) REFERENCES Cama(id_cama)
    )""",
    """CREATE TABLE Medico (
        id_medico SERIAL PRIMARY KEY,
        nombre_medico VARCHAR(255)
    )""",
    """CREATE TABLE Examen (
        id_examen SERIAL PRIMARY KEY,
        nombre_examen VARCHAR(255),
        tipo_examen VARCHAR(255)
    )""",
    """CREATE TABLE Diagnostico (
        id_diagnostico SERIAL PRIMARY KEY,
        id_paciente INT,
        id_medico INT,
        comentarios_diagnostico TEXT,
        fecha_diagnostico DATE,
        FOREIGN KEY (id_paciente) REFERENCES Paciente(id_paciente),
        FOREIGN KEY (id_medico) REFERENCES Medico(id_medico)
    )""",
    """CREATE TABLE Enfermedad (
        id_enfermedad SERIAL PRIMARY KEY,
        id_diagnostico INT,
        nombre_enfermedad VARCHAR(255),
        FOREIGN KEY (id_diagnostico) REFERENCES Diagnostico(id_diagnostico)
    )""",
    """CREATE TABLE Orden (
        id_orden SERIAL PRIMARY KEY,
        id_paciente INT,
        id_medico INT,
        id_examen INT,
        fecha_orden DATE,
        comentarios_orden TEXT,
        FOREIGN KEY (id_paciente) REFERENCES Paciente(id_paciente),
        FOREIGN KEY (id_medico) REFERENCES Medico(id_medico),
        FOREIGN KEY (id_examen) REFERENCES Examen(id_examen)
    )"""
]

try:
    # Conectar a la base de datos
    conexion = psycopg2.connect(**conexion_parametros)
    cursor = conexion.cursor()

    # Ejecutar cada sentencia SQL para crear las tablas
    for sentencia_sql in sentencias_sql:
        cursor.execute(sentencia_sql)
    conexion.commit()
    print("Tablas creadas con éxito")

except (Exception, Error) as error:
    print("Error al conectar o crear las tablas:", error)

finally:
    # Cerrar el cursor y la conexión
    if (conexion):
        cursor.close()
        conexion.close()
        print("Conexión con PostgreSQL cerrada")
