import psycopg2

################ Hay que importar la conexión a posgress.!!


# Cursor para ejecutar comandos SQL
cur = conn.cursor()

# Funciones para poblar la db
def insertar_habitacion():
    for _ in range(10):
        numero_habitacion = int(input("Ingresar número de habitación: "))
        ## %s es una caracteristica psycopg2 para evitar que se hagan inyecciones sql o que los datos se ingresen mal
        cur.execute("INSERT INTO Habitacion (numero_habitacion) VALUES (%s)", (numero_habitacion,))
    conn.commit()

def insertar_cama():
    for _ in range(10):
        numero_cama = int(input("Ingresar el número de la cama: "))
        id_habitacion = int(input("Ingresar el ID de la habitación: "))
        
        cur.execute("INSERT INTO Cama (numero_cama, id_habitacion) VALUES (%s, %s)", (numero_cama, id_habitacion))
    conn.commit()

def insertar_paciente():
    for _ in range(10):
        nombre_paciente = input("Ingresar el nombre del paciente: ")
        rut = input("Ingresar el RUT del paciente: ")
        fecha_ingreso = input("Ingresar la fecha de ingreso (YYYY-MM-DD): ")
        fecha_alta = input("Ingresar la fecha de alta (YYYY-MM-DD): ")
        id_cama = int(input("Ingresar el ID de la cama: "))
        cur.execute("INSERT INTO Paciente (nombre_paciente, rut, fecha_ingreso, fecha_alta, id_cama) VALUES (%s, %s, %s, %s, %s)", 
                    (nombre_paciente, rut, fecha_ingreso, fecha_alta, id_cama))
    conn.commit()

def insertar_medico():
    for _ in range(10):
        nombre_medico = input("Ingrese el nombre del médico: ")
        cur.execute("INSERT INTO Medico (nombre_medico) VALUES (%s)", (nombre_medico,))
    conn.commit()

def insertar_examen():
    for _ in range(10):
        nombre_examen = input("Ingrese el nombre del examen: ")
        tipo_examen = input("Ingrese el tipo del examen: ")
        cur.execute("INSERT INTO Examen (nombre_examen, tipo_examen) VALUES (%s, %s)", (nombre_examen, tipo_examen))
    conn.commit()

def insertar_diagnostico():
    for _ in range(10):
        id_paciente = int(input("Ingresar el ID del paciente: "))
        id_medico = int(input("Ingresar el ID del médico: "))
        comentarios_diagnostico = input("Ingresar los comentarios del diagnóstico: ")
        fecha_diagnostico = input("Ingresar la fecha del diagnóstico (YYYY-MM-DD): ")
        cur.execute("INSERT INTO Diagnostico (id_paciente, id_medico, comentarios_diagnostico, fecha_diagnostico) VALUES (%s, %s, %s, %s)", 
                    (id_paciente, id_medico, comentarios_diagnostico, fecha_diagnostico))
    conn.commit()

def insertar_enfermedad():
    for _ in range(10):
        id_diagnostico = int(input("Ingresar el ID del diagnóstico: "))
        nombre_enfermedad = input("Ingresar el nombre de la enfermedad: ")
        cur.execute("INSERT INTO Enfermedad (id_diagnostico, nombre_enfermedad) VALUES (%s, %s)", (id_diagnostico, nombre_enfermedad))
    conn.commit()

def insertar_orden():
    for _ in range(10):
        id_paciente = int(input("Ingresar el ID del paciente: "))
        id_medico = int(input("Ingresar el ID del médico: "))
        id_examen = int(input("Ingresar el ID del examen: "))
        fecha_orden = input("Ingresar la fecha de la orden (YYYY-MM-DD): ")
        comentarios_orden = input("Ingresar los comentarios de la orden: ")
        cur.execute("INSERT INTO Orden (id_paciente, id_medico, id_examen, fecha_orden, comentarios_orden) VALUES (%s, %s, %s, %s, %s)", 
                    (id_paciente, id_medico, id_examen, fecha_orden, comentarios_orden))
    conn.commit()


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
