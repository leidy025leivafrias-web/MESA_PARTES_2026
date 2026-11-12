def buscar_expedientes(expedientes):
    """
    Busca un expediente utilizando su código.
    """

    print("\n===================================")
    print("       BUSCAR EXPEDIENTE")
    print("===================================")

    if not expedientes:
        print("No existen expedientes registrados.")
        return

    codigo = input("Ingrese el código del expediente: ").strip().upper()

    for expediente in expedientes:
        if expediente["codigo"].upper() == codigo:

            print("\nExpediente encontrado:")
            print(f"Código: {expediente['codigo']}")
            print(f"Código del estudiante: {expediente['codigo_estudiante']}")
            print(f"Nivel educativo: {expediente['nivel']}")
            print(f"Estado: {expediente['estado']}")

            return expediente

    print("No se encontró ningún expediente con ese código.")
    return None