def Codigo_estudiante(estudiantes):
    while True:
        codigo = input("Ingrese el código del estudiante: ").strip().upper()

        if not codigo:
            print("Error: el código no puede estar vacío.")
            continue

        if estudiantes is None:
            return codigo

        encontrado = False

        for estudiante in estudiantes:
            if estudiante.get("codigo", "").upper() == codigo:
                encontrado = True
                break

        if encontrado:
            return codigo

        print("Error: no existe un estudiante con ese código.")
        print("Verifique el código e inténtelo nuevamente.")