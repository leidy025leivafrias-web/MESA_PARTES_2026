from padre import cargar_padres, guardar_padres

def eliminar_padre():
    print("\n--------------------------------")
    print("    ELIMINAR REGISTRO DE PADRE    ")
    print("\n--------------------------------")
    
    padres = cargar_padres()
    if not padres:
        print("No existen padres registrados.")
        return

    print("\n--- PADRES REGISTRADOS ---")
    for p in padres:
        print(f"Código: {p['codigo']} | Nombre: {p['nombres']} {p['paterno']} {p['materno']} | DNI: {p['dni']}")
    print("--------------------------")

    codigo = input("Ingrese el código del padre a eliminar: ").strip().upper()
    
    for i in range(len(padres)):
        if padres[i]["codigo"].upper() == codigo:
            p = padres[i]
            print(f"\nRegistro seleccionado: {p['nombres']} {p['paterno']} {p['materno']} (DNI: {p['dni']})")
            confirmacion = input("¿Está seguro de eliminar este registro? (SI/NO): ").strip().upper()
            
            if confirmacion == "SI":
                padres.pop(i)
                guardar_padres(padres)
                print("\nRegistro del padre eliminado correctamente")
            elif confirmacion == "NO":
                print("Eliminación cancelada")
            else:
                print("Respuesta no válida/ No se eliminó el registro")
            return
            
    print("No se encontró ningún padre con ese código")

