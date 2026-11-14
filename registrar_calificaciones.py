from validar_calificacion import validar_nota
def registrar_calificaciones(calificaciones, expedientes):
    print("\n===================================")
    print("     REGISTRAR CALIFICACIONES")
    print("===================================")
    if not expedientes:
        print("*No existen expedientes registrados.*")
        return
    pendientes = []
    for expediente in expedientes:
        tiene = False
        for registro in calificaciones:
             if registro ["codigo_expediente"] == expediente["codigo"]:
                  tiene = True
                  break
        if not tiene:
                  pendientes.append(expediente)
    if not pendientes:
        print("*Todos los expedientes ya tienen calificaciones.*")
        return
        
    print("\nExpediente sin calificaciones: ")
    for i, expediente in enumerate(pendientes, start=1):
        print(f"{i}. {expediente['codigo']} - Estudiante {expediente['codigo_estudiante']}")

    opcion = input("Seleccione el número: ").strip()
    if not opcion.isdigit() or not (1 <= int(opcion) <= len(pendientes)):
        print("*Opción no válida.*")
        return

    codigo = pendientes[int(opcion) - 1]["codigo"]

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