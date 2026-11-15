from familia import cargar_familias, guardar_familias

def eliminar_familia():
    print("\n------------------------------------------")
    print("        ELIMINAR VÍNCULO FAMILIAR         ")
    print("------------------------------------------")
    
    familias = cargar_familias()
    if not familias:
        print("No existen familias registradas")
        return

    print("\n--- FAMILIAS REGISTRADAS ---")
    for f in familias:
        print(f"Familia: {f['codigo_familia']} | Padre: {f['codigo_padre']} | Madre: {f['codigo_madre']} | Estudiante: {f['codigo_estudiante']}")
    print("----------------------------")

    codigo = input("Ingrese el código de familia a eliminar: ").strip().upper()
    
    for i in range(len(familias)):
        if familias[i]["codigo_familia"].upper() == codigo:
            f = familias[i]
            print(f"\nRegistro seleccionado: {codigo} (Padre: {f['codigo_padre']}, Madre: {f['codigo_madre']}, Estudiante: {f['codigo_estudiante']})")
            confirmacion = input("¿Está seguro de eliminar este vínculo familiar? (SI/NO): ").strip().upper()
            
            if confirmacion == "SI":
                familias.pop(i)
                guardar_familias(familias)
                print("\nVínculo familiar eliminado correctamente")
            elif confirmacion == "NO":
                print("Eliminación cancelada")
            else:
                print("Respuesta no válida/ No se eliminó el registro")
            return
            
    print("No se encontró ninguna familia con ese código")

