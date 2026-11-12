from validar_calificacion import validar_nota
def modificar_calificacion(calificaciones):

    print("\n===================================")
    print("       MODIFICAR CALIFICACIÓN")
    print("===================================")

    if not calificaciones:
        print("*No existen calificaciones registradas.*")
        return
    codigo = input("Ingrese el código del expediente: ").strip().upper()
    for registro in calificaciones:
        if registro["codigo_expediente"].upper() == codigo:
            print("\nSeleccione la calificación que desea modificar:")
            print("1. Primer bimestre")
            print("2. Segundo bimestre")
            print("3. Tercer bimestre")
            print("4. Cuarto bimestre")
            opcion = input("Seleccione una opción: ").strip()
            bimestres = {
                "1": "bimestre1",
                "2": "bimestre2",
                "3": "bimestre3",
                "4": "bimestre4"
            }

            if opcion not in bimestres:
                print("Error: seleccione una opción válida.")
                return
            clave = bimestres[opcion]
            print(f"Nota actual: {registro[clave]:.2f}")
            nueva_nota = validar_nota(opcion)
            registro[clave] = nueva_nota
            print("\n*Calificación modificada correctamente.*")
            return
    print("*No se encontraron calificaciones para ese expediente.*")