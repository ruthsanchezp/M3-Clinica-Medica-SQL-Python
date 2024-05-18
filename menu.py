from conexion import connect_db
import controlador

def mostrar_menu():
    print("\n--- Menú ---")
    print("1. Mostrar todos los pacientes")
    print("2. Mostrar detalle de un paciente por RUT")
    print("3. Cambiar a un paciente de cama")
    print("4. Cambiar a un paciente de médico")
    print("5. Crear una nueva habitación")
    print("6. Crear una nueva cama")
    print("7. Salir")

def menu():
    conn = connect_db()
    if not conn:
        print("No se pudo conectar a la base de datos. Saliendo del programa.")
        return

    cursor = conn.cursor()

    while True:
        mostrar_menu()
        opcion = input("Seleccione opción: ")

        match opcion:
            case '1':
                controlador.mostrar_pacientes(cursor)
            case '2':
                rut = input("Ingrese el RUT del paciente: ")
                controlador.mostrar_detalle_paciente(cursor, rut)
            case '3':
                rut = input("Ingrese el RUT del paciente: ")
                numero_cama = input("Ingrese el número de la nueva cama: ")
                numero_habitacion = input("Ingrese el número de la habitación: ")
                controlador.cambiar_cama(cursor, rut, numero_cama, numero_habitacion)
                conn.commit()
            case '4':
                rut = input("Ingrese el RUT del paciente: ")
                nuevo_medico = input("Ingrese el ID del nuevo médico: ")
                controlador.cambiar_medico(cursor, rut, nuevo_medico)
                conn.commit()
            case '5':
                numero_habitacion = input("Ingrese el número de la nueva habitación: ")
                controlador.crear_habitacion(cursor, numero_habitacion)
                conn.commit()
            case '6':
                numero_cama = input("Ingrese el número de la nueva cama: ")
                numero_habitacion = input("Ingrese el número de la habitación: ")
                controlador.crear_cama(cursor, numero_cama, numero_habitacion)
                conn.commit()
            case '7':
                cursor.close()
                conn.close()
                break
            case _:
                print("Opción no válida, intente de nuevo.")

if __name__ == "__main__":
    menu()
