def validar_estado():
    estados = {
        "1": "Pendiente",
        "2": "En proceso",
        "3": "Finalizado"
    }

    while True:
        print("\n--- ESTADO DEL EXPEDIENTE ---")
        print("1. Pendiente")
        print("2. En proceso")
        print("3. Finalizado")

        opcion = input("Seleccione el estado: ").strip()

        if opcion in estados:
            return estados[opcion]

        print("Error: seleccione una opción válida.")