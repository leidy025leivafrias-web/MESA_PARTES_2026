from Codigo_estudiante import Codigo_estudiante
from nivel_educativo import nivel_educativo
def modificar_expediente(expedientes, estudiantes=None):

    print("\n===================================")
    print("       MODIFICAR EXPEDIENTE")
    print("===================================")

    if not expedientes:
        print("No existen expedientes registrados.")
        return

    codigo = input("Ingrese el código del expediente: ").strip().upper()

    for expediente in expedientes:

        if expediente["codigo"].upper() == codigo:

            print("\nExpediente encontrado.")
            print("1. Modificar código del estudiante")
            print("2. Modificar nivel educativo")
            print("3. Modificar ambos datos")
            print("4. Cancelar")

            opcion = input("Seleccione una opción: ").strip()

            if opcion in ("1", "3"):

                nuevo_codigo = Codigo_estudiante(estudiantes)

                # Comprobar que el nuevo estudiante no tenga
                # otro expediente registrado.
                duplicado = any(
                    otro["codigo_estudiante"] == nuevo_codigo
                    and otro["codigo"] != codigo
                    for otro in expedientes
                )

                if duplicado:
                    print("Error: el estudiante ya tiene otro expediente.")
                    return

                expediente["codigo_estudiante"] = nuevo_codigo

            if opcion in ("2", "3"):
                expediente["nivel"] = nivel_educativo()

            if opcion == "4":
                print("Modificación cancelada.")
                return

            if opcion not in ("1", "2", "3", "4"):
                print("Opción no válida.")
                return

            print("\nExpediente modificado correctamente.")
            return

    print("No se encontró el expediente solicitado.")