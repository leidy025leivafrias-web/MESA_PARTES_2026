def calcular_promedio(registro):
    print("-" * 50)
    print("      CONDICIÓN DEL ESTUDIANTE")
    print("-" * 50)

    bimestre1 = float(registro["bimestre1"])
    bimestre2 = float(registro["bimestre2"])
    bimestre3 = float(registro["bimestre3"])
    bimestre4 = float(registro["bimestre4"])

    promedio = (bimestre1 + bimestre2 + bimestre3 + bimestre4) / 4
    print (f"PROMEDIO FINAL ANUAL: {promedio:.2f}")

    if promedio < 13:
        print("CONDICIÓN DEL ESTUDIANTE: DESAPROBADO")
    else:
        print("CONDICIÓN DEL ESTUDIANTE: APROBADO ")
        
    return promedio