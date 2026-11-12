def nivel_educativo():
    while True:
        print("\nNIVEL EDUCATIVO")
        print("1. Inicial")
        print("2. Primaria")
        print("3. Secundaria")
        print("4. EBE (Educación Básica Especial)")

        opcion = input("INGRESE LA OPCIÓN (1-4): ").strip()

        if not opcion:
            print("*ERROR: No puede dejar la opción en blanco.*\n")
        elif opcion == "1":
            return "Inicial"
        elif opcion == "2":
            return "Primaria"
        elif opcion == "3":
            return "Secundaria"
        elif opcion == "4":
            return "EBE (Educación Básica Especial)"
        else:
            print("*ERROR: Opción no válida. Ingrese un número entre 1 y 4.*\n")