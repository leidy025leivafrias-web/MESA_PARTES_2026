def buscar_calificaciones(calificaciones):
    print("\n===================================")
    print("      BUSCAR CALIFICACIONES")
    print("===================================")

    if not calificaciones:
        print("*No existen calificaciones registradas.*")
        return

    codigo = input("Ingrese el código del expediente: ").strip().upper()

    for registro in calificaciones:

        if registro["codigo_expediente"].upper() == codigo:

            print("\nCALIFICACIONES ENCONTRADAS:")
            print(f"- Código del expediente: {codigo}")
            print(f"- Primer bimestre: {registro['bimestre1']:.2f}")
            print(f"- Segundo bimestre: {registro['bimestre2']:.2f}")
            print(f"- Tercer bimestre: {registro['bimestre3']:.2f}")
            print(f"- Cuarto bimestre: {registro['bimestre4']:.2f}")

            return registro

    print("*No se encontraron calificaciones del estudiante.*")
    return None