import psycopg2

HOST = 'localhost'
DATABASE = 'Pacientes2'
USER = 'postgres'
PASSWORD = 'doite2323'

# Configurar la conexión a la base de datos
def connect_db():
    return psycopg2.connect(
        dbname=DATABASE,
        user=USER,
        password=PASSWORD,
        host=HOST,
    )

# Conexión y cursor para ejecutar comandos SQL
conn = connect_db()
cur = conn.cursor()

# Funciones para poblar la base de datos
def insertar_habitacion():
    while True:
        try:
            numero_habitacion = int(input("Ingresar número de habitación: "))
            cur.execute("INSERT INTO Habitacion (numero_habitacion) VALUES (%s)", (numero_habitacion,))
            conn.commit()
        except Exception as e:
            print(f"Error al insertar habitación: {e}")
            conn.rollback()
        if input("¿Desea ingresar otra habitación? (s/n): ").lower() != 's':
            break

def insertar_cama():
    while True:
        try:
            numero_cama = int(input("Ingresar el número de la cama: "))
            numero_habitacion = int(input("Ingresar el número de la habitación: "))
            
            cur.execute("SELECT id_habitacion FROM Habitacion WHERE numero_habitacion = %s", (numero_habitacion,))
            id_habitacion = cur.fetchone()
            
            if id_habitacion:
                id_habitacion = id_habitacion[0]
                cur.execute("INSERT INTO Cama (numero_cama, id_habitacion) VALUES (%s, %s)", (numero_cama, id_habitacion))
                conn.commit()
                print(f"Cama insertada con éxito en la habitación ID: {id_habitacion}")
            else:
                print(f"No se encontró una habitación con el número {numero_habitacion}")
        except Exception as e:
            print(f"Error al insertar cama: {e}")
            conn.rollback()
        if input("¿Desea ingresar otra cama? (s/n): ").lower() != 's':
            break

def insertar_paciente():
    while True:
        try:
            nombre_paciente = input("Ingresar el nombre del paciente: ")
            rut = input("Ingresar el RUT del paciente: ")
            fecha_ingreso = input("Ingresar la fecha de ingreso (YYYY-MM-DD): ")
            fecha_alta = input("Ingresar la fecha de alta (YYYY-MM-DD): ")
            id_cama = int(input("Ingresar el ID de la cama: "))
            cur.execute("INSERT INTO Paciente (nombre_paciente, rut, fecha_ingreso, fecha_alta, id_cama) VALUES (%s, %s, %s, %s, %s)", 
                        (nombre_paciente, rut, fecha_ingreso, fecha_alta, id_cama))
            conn.commit()
        except Exception as e:
            print(f"Error al insertar paciente: {e}")
            conn.rollback()
        if input("¿Desea ingresar otro paciente? (s/n): ").lower() != 's':
            break

def insertar_medico():
    while True:
        try:
            nombre_medico = input("Ingrese el nombre del médico: ")
            cur.execute("INSERT INTO Medico (nombre_medico) VALUES (%s)", (nombre_medico,))
            conn.commit()
        except Exception as e:
            print(f"Error al insertar médico: {e}")
            conn.rollback()
        if input("¿Desea ingresar otro médico? (s/n): ").lower() != 's':
            break

def insertar_examen():
    while True:
        try:
            nombre_examen = input("Ingrese el nombre del examen: ")
            tipo_examen = input("Ingrese el tipo del examen: ")
            cur.execute("INSERT INTO Examen (nombre_examen, tipo_examen) VALUES (%s, %s)", (nombre_examen, tipo_examen))
            conn.commit()
        except Exception as e:
            print(f"Error al insertar examen: {e}")
            conn.rollback()
        if input("¿Desea ingresar otro examen? (s/n): ").lower() != 's':
            break

def insertar_diagnostico():
    while True:
        try:
            id_paciente = int(input("Ingresar el ID del paciente: "))
            id_medico = int(input("Ingresar el ID del médico: "))
            comentarios_diagnostico = input("Ingresar los comentarios del diagnóstico: ")
            fecha_diagnostico = input("Ingresar la fecha del diagnóstico (YYYY-MM-DD): ")
            cur.execute("INSERT INTO Diagnostico (id_paciente, id_medico, comentarios_diagnostico, fecha_diagnostico) VALUES (%s, %s, %s, %s)", 
                        (id_paciente, id_medico, comentarios_diagnostico, fecha_diagnostico))
            conn.commit()
        except Exception as e:
            print(f"Error al insertar diagnóstico: {e}")
            conn.rollback()
        if input("¿Desea ingresar otro diagnóstico? (s/n): ").lower() != 's':
            break

def insertar_enfermedad():
    while True:
        try:
            id_diagnostico = int(input("Ingresar el ID del diagnóstico: "))
            nombre_enfermedad = input("Ingresar el nombre de la enfermedad: ")
            cur.execute("INSERT INTO Enfermedad (id_diagnostico, nombre_enfermedad) VALUES (%s, %s)", (id_diagnostico, nombre_enfermedad))
            conn.commit()
        except Exception as e:
            print(f"Error al insertar enfermedad: {e}")
            conn.rollback()
        if input("¿Desea ingresar otra enfermedad? (s/n): ").lower() != 's':
            break

def insertar_orden():
    while True:
        try:
            id_paciente = int(input("Ingresar el ID del paciente: "))
            id_medico = int(input("Ingresar el ID del médico: "))
            id_examen = int(input("Ingresar el ID del examen: "))
            fecha_orden = input("Ingresar la fecha de la orden (YYYY-MM-DD): ")
            comentarios_orden = input("Ingresar los comentarios de la orden: ")
            cur.execute("INSERT INTO Orden (id_paciente, id_medico, id_examen, fecha_orden, comentarios_orden) VALUES (%s, %s, %s, %s, %s)", 
                        (id_paciente, id_medico, id_examen, fecha_orden, comentarios_orden))
            conn.commit()
        except Exception as e:
            print(f"Error al insertar orden: {e}")
            conn.rollback()
        if input("¿Desea ingresar otra orden? (s/n): ").lower() != 's':
            break

# Llamar a las funciones
insertar_habitacion()
insertar_cama()
insertar_paciente()
insertar_medico()
insertar_examen()
insertar_diagnostico()
insertar_enfermedad()
insertar_orden()

# Cerrar la conexión
cur.close()
conn.close()
