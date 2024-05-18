from datetime import date

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

def cambiar_cama(cursor, rut, numero_cama, numero_habitacion):
    id_cama = obtener_id_cama(cursor, numero_cama, numero_habitacion)
    if not id_cama:
        print(f"No se encontró una cama con el número {numero_cama} en la habitación {numero_habitacion}.")
        return

    query = "UPDATE Paciente SET id_cama = %s WHERE rut = %s"
    cursor.execute(query, (id_cama, rut))
    print("Cama cambiada exitosamente.")

def cambiar_medico(cursor, rut, nuevo_medico):
    cursor.execute("SELECT id_paciente FROM Paciente WHERE rut = %s", (rut,))
    result = cursor.fetchone()
    
    if result:
        id_paciente = result[0]
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

def crear_habitacion(cursor, numero_habitacion):
    query = "INSERT INTO Habitacion (numero_habitacion) VALUES (%s)"
    cursor.execute(query, (numero_habitacion,))
    print("Habitación creada exitosamente.")

def crear_cama(cursor, numero_cama, numero_habitacion):
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
