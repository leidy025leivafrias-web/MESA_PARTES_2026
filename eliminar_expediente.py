def eliminar_expediente(expedientes):
    print("\n===================================")
    print("       ELIMINAR EXPEDIENTE")
    print("===================================")

    if not expedientes:
        print("No existen expedientes registrados.")
        return

    codigo = input("Ingrese el código del expediente: ").strip().upper()

    for indice, expediente in enumerate(expedientes):

        if expediente["codigo"].upper() == codigo:

            print("\nExpediente encontrado.")
            print(f"Código: {expediente['codigo']}")
            print(f"Estudiante: {expediente['codigo_estudiante']}")

            confirmacion = input(
                "¿Está seguro de eliminarlo? (SI/NO): "
            ).strip().upper()

            if confirmacion == "SI":
                expedientes.pop(indice)
                print("Expediente eliminado correctamente.")

            elif confirmacion == "NO":
                print("Eliminación cancelada.")

            else:
                print("Respuesta no válida. No se eliminó el expediente.")

            return

    print("No se encontró el expediente solicitado.")