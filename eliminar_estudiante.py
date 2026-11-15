from estudiantes import cargar_estudiantes, guardar_estudiantes

def eliminar_estudiante():
    print("\n-----------------------------------------")
    print("     ELIMINAR REGISTRO DEL ESTUDIANTE     ")
    print("------------------------------------------")
    
    estudiantes = cargar_estudiantes()
    if not estudiantes:
        print("No existen estudiantes registrados")
        return

    print("\n--- ESTUDIANTES REGISTRADOS ---")
    for e in estudiantes:
        print(f"Código: {e['codigo']} | Nombre: {e['nombres']} {e['paterno']} {e['materno']} | DNI: {e['dni']}")
    print("-------------------------------")

    codigo = input("Ingrese el código del estudiante a eliminar: ").strip().upper()
    
    for i in range(len(estudiantes)):
        if estudiantes[i]["codigo"].upper() == codigo:
            e = estudiantes[i]
            print(f"\nRegistro seleccionado: {e['nombres']} {e['paterno']} {e['materno']} (Nivel: {e['nivel']})")
            confirmacion = input("¿Está seguro de eliminar este registro? (SI/NO): ").strip().upper()
            
            if confirmacion == "SI":
                estudiantes.pop(i)
                guardar_estudiantes(estudiantes)
                print("Registro del estudiante eliminado correctamente")
            elif confirmacion == "NO":
                print("Eliminación cancelada.")
            else:
                print("Respuesta no válida/ No se eliminó el registro.")
            return
            
    print("No se encontró ningún estudiante con ese código")

