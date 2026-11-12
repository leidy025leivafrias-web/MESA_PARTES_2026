def validar_codigo_expediente(expedientes):
    while True:
        codigo = input("Ingrese el código del expediente: ").strip().upper()

        if not codigo:
            print("*Error: el código no puede estar vacío.*")
            continue

        existe = any(expediente["codigo"].upper() == codigo
        for expediente in expedientes
        )

        if existe:
            return codigo

        print("*Error: no existe un expediente con ese código.*")