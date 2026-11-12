
def listar_calificaciones(calificaciones):
    if not calificaciones:
        print("*No hay calificaciones para mostrar.*")
        return

    for numero, registro in enumerate(calificaciones, start=1):

        nota1 = registro["bimestre1"]
        nota2 = registro["bimestre2"]
        nota3 = registro["bimestre3"]
        nota4 = registro["bimestre4"]

        promedio = (nota1 + nota2 + nota3 + nota4) / 4

        if promedio >= 13:
            condicion = "Aprobado"
        else:
            condicion = "Desaprobado"

        print(f"\n CALIFICACIONES N° {numero}")
        print("CODIGO DEL EXPEDIENTE: ", registro["codigo_expediente"])
        print("NOTA 1: ", nota1)
        print("NOTA 2: ", nota2)
        print("NOTA 3: ", nota3)
        print("NOTA 4: ", nota4)
        print(f"PROMEDIO: {promedio:.2f}")
        print("CONDICIÓN: ", condicion)
        print("-" * 50)

    print("\nTOTAL DE REGISTROS: ", len(calificaciones))
