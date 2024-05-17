import psycopg2
from psycopg2 import Error
from datetime import date
import config

# Configurar la conexión a la base de datos con los datos del archivo config.py
def connect_db():
    return psycopg2.connect(
        dbname=config.DATABASE,
        user=config.USER,
        password=config.PASSWORD,
        host=config.HOST,
    )

# Conexión y cursor para ejecutar comandos SQL
conn = connect_db()
cur = conn.cursor()

# Mostrar todos los pacientes
def mostrar_pacientes(conn):
    cursor = conn.cursor()
    query = """
    SELECT Paciente.rut, Paciente.nombre_paciente, Enfermedad.nombre_enfermedad, Medico.nombre_medico, Habitacion.numero_habitacion
    FROM Paciente
    JOIN Cama ON Paciente.id_cama = Cama.id_cama
    JOIN Habitacion ON Cama.id_habitacion = Habitacion.id_habitacion
    JOIN Diagnostico ON Paciente.id_paciente = Diagnostico.id_paciente
    JOIN Medico ON Diagnostico.id_medico = Medico.id_medico
    JOIN Enfermedad ON Diagnostico.id_diagnostico = Enfermedad.id_diagnostico
    """
    cursor.execute(query)
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()

# Mostrar detalle de un paciente por rut
def mostrar_detalle_paciente(conn, rut):
    cursor = conn.cursor()
    query = """
    SELECT Paciente.rut, Paciente.nombre_paciente, Enfermedad.nombre_enfermedad, Medico.nombre_medico, COALESCE(Examen.nombre_examen, 'No realizado'), Habitacion.numero_habitacion, Cama.numero_cama
    FROM Paciente
    JOIN Cama ON Paciente.id_cama = Cama.id_cama
    JOIN Habitacion ON Cama.id_habitacion = Habitacion.id_habitacion
    JOIN Diagnostico ON Paciente.id_paciente = Diagnostico.id_paciente
    JOIN Medico ON Diagnostico.id_medico = Medico.id_medico
    JOIN Enfermedad ON Diagnostico.id_diagnostico = Enfermedad.id_diagnostico
    LEFT JOIN Orden ON Paciente.id_paciente = Orden.id_paciente
    LEFT JOIN Examen ON Orden.id_examen = Examen.id_examen
    WHERE Paciente.rut = %s
    """
    cursor.execute(query, (rut,))
    row = cursor.fetchone()
    if row:
        print(row)
    else:
        print("Paciente no encontrado.")
    cursor.close()

# Obtener id_cama a partir de numero_cama y numero_habitacion
def obtener_id_cama(conn, numero_cama, numero_habitacion):
    cursor = conn.cursor()
    query = """
    SELECT Cama.id_cama
    FROM Cama
    JOIN Habitacion ON Cama.id_habitacion = Habitacion.id_habitacion
    WHERE Cama.numero_cama = %s AND Habitacion.numero_habitacion = %s
    """
    cursor.execute(query, (numero_cama, numero_habitacion))
    result = cursor.fetchone()
    cursor.close()
    return result[0] if result else None

# Cambiar a un paciente de cama
def cambiar_cama(conn, rut, numero_cama, numero_habitacion):
    id_cama = obtener_id_cama(conn, numero_cama, numero_habitacion)
    if not id_cama:
        print(f"No se encontró una cama con el número {numero_cama} en la habitación {numero_habitacion}.")
        return

    cursor = conn.cursor()
    query = "UPDATE Paciente SET id_cama = %s WHERE rut = %s"
    cursor.execute(query, (id_cama, rut))
    conn.commit()
    print("Cama cambiada exitosamente.")
    cursor.close()

def cambiar_medico(conn, rut, nuevo_medico):
    cursor = conn.cursor()
    
    # Obtener id_paciente y el id del diagnóstico más reciente
    cursor.execute("SELECT id_paciente FROM Paciente WHERE rut = %s", (rut,))
    result = cursor.fetchone()
    
    if result:
        id_paciente = result[0]
        
        # Actualizar el médico en el diagnóstico más reciente
        query = """
        UPDATE Diagnostico
        SET id_medico = %s, comentarios_diagnostico = %s, fecha_diagnostico = %s
        WHERE id_paciente = %s
        AND fecha_diagnostico = (SELECT MAX(fecha_diagnostico) FROM Diagnostico WHERE id_paciente = %s)
        """
        cursor.execute(query, (nuevo_medico, 'Médico actualizado', date.today(), id_paciente, id_paciente))
        conn.commit()
        print("Médico cambiado exitosamente.")
    else:
        print("Paciente no encontrado.")
    
    cursor.close()

# Crear una nueva habitación
def crear_habitacion(conn, numero_habitacion):
    cursor = conn.cursor()
    query = "INSERT INTO Habitacion (numero_habitacion) VALUES (%s)"
    cursor.execute(query, (numero_habitacion,))
    conn.commit()
    print("Habitación creada exitosamente.")
    cursor.close()

# Crear una nueva cama
def crear_cama(conn, numero_cama, id_habitacion):
    cursor = conn.cursor()
    query = "INSERT INTO Cama (numero_cama, id_habitacion) VALUES (%s, %s)"
    cursor.execute(query, (numero_cama, id_habitacion))
    conn.commit()
    print("Cama creada exitosamente.")
    cursor.close()

# Menú de la consola
def menu():
    conn = connect_db()
    while True:
        print("\n--- Menú ---")
        print("1. Mostrar todos los pacientes")
        print("2. Mostrar detalle de un paciente por RUT")
        print("3. Cambiar a un paciente de cama")
        print("4. Cambiar a un paciente de médico")
        print("5. Crear una nueva habitación")
        print("6. Crear una nueva cama")
        print("7. Salir")
        
        opcion = input("Seleccione opción: ")

        match opcion:
            case '1':
                mostrar_pacientes(conn)
            case '2':
                rut = input("Ingrese el RUT del paciente: ")
                mostrar_detalle_paciente(conn, rut)
            case '3':
                rut = input("Ingrese el RUT del paciente: ")
                numero_cama = input("Ingrese el número de la nueva cama: ")
                numero_habitacion = input("Ingrese el número de la habitación: ")
                cambiar_cama(conn, rut, numero_cama, numero_habitacion)
            case '4':
                rut = input("Ingrese el RUT del paciente: ")
                nuevo_medico = input("Ingrese el ID del nuevo médico: ")
                cambiar_medico(conn, rut, nuevo_medico)
            case '5':
                numero_habitacion = input("Ingrese el número de la nueva habitación: ")
                crear_habitacion(conn, numero_habitacion)
            case '6':
                numero_cama = input("Ingrese el número de la nueva cama: ")
                id_habitacion = input("Ingrese el ID de la habitación: ")
                crear_cama(conn, numero_cama, id_habitacion)
            case '7':
                conn.close()
                break
            case _:
                print("Opción no válida, intente de nuevo.")

if __name__ == "__main__":
    menu()
