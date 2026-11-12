
def validar_nota(numero_bimestre):
    while True:
        try:
            nota = float(input(f"Ingrese la nota del {numero_bimestre}° bimestre: "))
            if 0 <= nota <= 20:
                return nota
            print("*Error: la nota debe estar entre 0 y 20.*")
        except ValueError:
            print("*Error: debe ingresar un valor numérico.*")
