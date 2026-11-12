def nota_maxima(registro):
    bimestre1 = float(registro["bimestre1"])
    bimestre2 = float(registro["bimestre2"])
    bimestre3 = float(registro["bimestre3"])
    bimestre4 = float(registro["bimestre4"])

    maxima = max(bimestre1, bimestre2, bimestre3, bimestre4)
    print(f"NOTA MÁXIMA: {maxima:.2f}")

    return maxima