def Codigo_expediente(expedientes):
    numero = len(expedientes) + 1
    while True:
        codigo = f"EXP{numero:03d}"
        existe = False

        for expediente in expedientes:
            if expediente["codigo"] == codigo:
                existe = True
                break

        if existe:
            numero += 1
        else:
            return codigo