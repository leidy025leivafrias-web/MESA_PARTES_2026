def eliminar_calificaciones(calificaciones):
    print("\n===================================")
    print("      ELIMINAR CALIFICACIONES")
    print("===================================")

    if not calificaciones:
        print("*No existen calificaciones registradas.*")
        return
    codigo = input("Ingrese el código del expediente: ").strip().upper()
    for indice, registro in enumerate(calificaciones):
        if registro["codigo_expediente"].upper() == codigo:
            confirmacion = input("¿Está seguro de eliminar las calificaciones? (SI/NO): ").strip().upper()
            if confirmacion == "SI":
                calificaciones.pop(indice)
                print("*Calificaciones eliminadas correctamente.*")
            elif confirmacion == "NO":
                print("*Eliminación cancelada.*")
            else:
                print("*Respuesta no válida. No se eliminó el registro.*")

            return
    print("*No se encontraron calificaciones para ese expediente.*")