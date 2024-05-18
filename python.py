import psycopg2
from datetime import date
import config
        
def connect_db():
    return psycopg2.connect(
         dbname=config.DATABASE,
         user=config.USER,
         password=config.PASSWORD,
         host=config.HOST,
    )

        # Mostrar todos los pacientes
def mostrar_pacientes(cursor):
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

# Mostrar detalle de un paciente por rut
def mostrar_detalle_paciente(cursor, rut):
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

# Obtener id_cama a partir de numero_cama y numero_habitacion
def obtener_id_cama(cursor, numero_cama, numero_habitacion):
    query = """
    SELECT Cama.id_cama
    FROM Cama
    JOIN Habitacion ON Cama.id_habitacion = Habitacion.id_habitacion
    WHERE Cama.numero_cama = %s AND Habitacion.numero_habitacion = %s
    """
    cursor.execute(query, (numero_cama, numero_habitacion))
    result = cursor.fetchone()
    return result[0] if result else None

# Cambiar a un paciente de cama
def cambiar_cama(cursor, rut, numero_cama, numero_habitacion):
    id_cama = obtener_id_cama(cursor, numero_cama, numero_habitacion)
    if not id_cama:
        print(f"No se encontró una cama con el número {numero_cama} en la habitación {numero_habitacion}.")
        return

    query = "UPDATE Paciente SET id_cama = %s WHERE rut = %s"
    cursor.execute(query, (id_cama, rut))
    print("Cama cambiada exitosamente.")

def cambiar_medico(cursor, rut, nuevo_medico):
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
        print("Médico cambiado exitosamente.")
    else:
        print("Paciente no encontrado.")

# Crear una nueva habitación
def crear_habitacion(cursor, numero_habitacion):
    query = "INSERT INTO Habitacion (numero_habitacion) VALUES (%s)"
    cursor.execute(query, (numero_habitacion,))
    print("Habitación creada exitosamente.")

# Crear una nueva cama
def crear_cama(cursor, numero_cama, numero_habitacion):
    # Obtener id_habitacion a partir del numero_habitacion
    query = "SELECT id_habitacion FROM Habitacion WHERE numero_habitacion = %s"
    cursor.execute(query, (numero_habitacion,))
    result = cursor.fetchone()
    
    if result:
        id_habitacion = result[0]
        query = "INSERT INTO Cama (numero_cama, id_habitacion) VALUES (%s, %s)"
        cursor.execute(query, (numero_cama, id_habitacion))
        print("Cama creada exitosamente.")
    else:
        print(f"No se encontró una habitación con el número {numero_habitacion}.")

# Menú de la consola
def menu():
    conn = connect_db()
    if not conn:
        print("No se pudo conectar a la base de datos. Saliendo del programa.")
        return

    cursor = conn.cursor()

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
                mostrar_pacientes(cursor)
            case '2':
                rut = input("Ingrese el RUT del paciente: ")
                mostrar_detalle_paciente(cursor, rut)
            case '3':
                rut = input("Ingrese el RUT del paciente: ")
                numero_cama = input("Ingrese el número de la nueva cama: ")
                numero_habitacion = input("Ingrese el número de la habitación: ")
                cambiar_cama(cursor, rut, numero_cama, numero_habitacion)
                conn.commit()
            case '4':
                rut = input("Ingrese el RUT del paciente: ")
                nuevo_medico = input("Ingrese el ID del nuevo médico: ")
                cambiar_medico(cursor, rut, nuevo_medico)
                conn.commit()
            case '5':
                numero_habitacion = input("Ingrese el número de la nueva habitación: ")
                crear_habitacion(cursor, numero_habitacion)
                conn.commit()
            case '6':
                numero_cama = input("Ingrese el número de la nueva cama: ")
                numero_habitacion = input("Ingrese el número de la habitación: ")
                crear_cama(cursor, numero_cama, numero_habitacion)
                conn.commit()
            case '7':
                cursor.close()
                conn.close()
                break
            case _:
                print("Opción no válida, intente de nuevo.")

if __name__ == "__main__":
    menu()
