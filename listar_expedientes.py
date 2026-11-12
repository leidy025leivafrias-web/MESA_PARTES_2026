def listado_expedientes(expedientes):
    if not expedientes:
        print("No hay expedientes para mostrar.")
        return
    
    for numero, expediente in enumerate(expedientes,start=1):
        print(f"\n EXPEDIENTE N° {numero}")
        print("CODIGO: ", expediente["codigo"])
        print("DNI DEL ESTUDIANTE: ", expediente["dni_estudiante"])
        print("ESTUDIANTE: ", expediente["nombre_estudiante"],expediente["paterno_estudiante"], expediente["materno_estudiante"])
        print("NIVEL EDUCATIVO: ",expediente["nivel"])
        print("ESTADO: ",expediente["estado"])
        print("-"*50)

    print("\nTOTAL DE EXPEDIENTES: ", len(expedientes))