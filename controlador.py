import modelo

def mostrar_pacientes(cursor):
    modelo.mostrar_pacientes(cursor)

def mostrar_detalle_paciente(cursor, rut):
    modelo.mostrar_detalle_paciente(cursor, rut)

def cambiar_cama(cursor, rut, numero_cama, numero_habitacion):
    modelo.cambiar_cama(cursor, rut, numero_cama, numero_habitacion)

def cambiar_medico(cursor, rut, nuevo_medico):
    modelo.cambiar_medico(cursor, rut, nuevo_medico)

def crear_habitacion(cursor, numero_habitacion):
    modelo.crear_habitacion(cursor, numero_habitacion)

def crear_cama(cursor, numero_cama, numero_habitacion):
    modelo.crear_cama(cursor, numero_cama, numero_habitacion)
