def listado_expedientes(expedientes):
    if not expedientes:
        print("No hay expedientes para mostrar.")
        return

    print("\n===================================")
    print("       LISTADO DE EXPEDIENTES")
    print("===================================")

    for numero, expediente in enumerate(expedientes,start=1):

        print(f"\n EXPEDIENTE N° {numero}")
        print("CODIGO: ", expediente["codigo"])
        print("CODIGO DEL ESTUDIANTE: ", expediente["codigo_estudiante"])
        print("NIVEL EDUCATIVO: ",expediente["nivel"])
        print("-"*50)

    print("\nTOTAL DE EXPEDIENTES: ", len(expedientes))