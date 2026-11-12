def actualizar_estado_tramite(expedientes):

    print("\n===================================")
    print("      ACTUALIZAR ESTADO")
    print("===================================")

    if not expedientes:
        print("No existen expedientes registrados.")
        return

    codigo = input("Ingrese el código del expediente: ").strip().upper()

    for expediente in expedientes:

        if expediente["codigo"].upper() == codigo:

            print(f"\nEstado actual: {expediente['estado']}")

            nuevo_estado = nuevo_estado()

            expediente["estado"] = nuevo_estado

            print("\nEstado actualizado correctamente.")
            return

    print("No se encontró el expediente solicitado.")
