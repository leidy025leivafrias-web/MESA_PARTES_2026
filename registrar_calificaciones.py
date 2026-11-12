from Codigo_expediente import Codigo_expediente
from validar_calificacion import validar_nota
def registrar_calificaciones(calificaciones, expedientes):
    print("\n===================================")
    print("     REGISTRAR CALIFICACIONES")
    print("===================================")
    if not expedientes:
        print("*No existen expedientes registrados.*")
        return

    codigo = Codigo_expediente(expedientes)

    for registro in calificaciones:
        if registro["codigo_expediente"] == codigo:
            print("*Error: este expediente ya tiene calificaciones registradas.*")
            return
    print("\nIngrese las cuatro calificaciones:")
    bimestre1 = validar_nota(1)
    bimestre2 = validar_nota(2)
    bimestre3 = validar_nota(3)
    bimestre4 = validar_nota(4)

    registro = {
        "codigo_expediente": codigo,
        "bimestre1": bimestre1,
        "bimestre2": bimestre2,
        "bimestre3": bimestre3,
        "bimestre4": bimestre4
    }

    calificaciones.append(registro)
    print("\n*Calificaciones registradas correctamente.*")