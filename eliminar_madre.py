from madre import cargar_madres, guardar_madres

def eliminar_madre():
    print("\n--------------------------------")
    print("    ELIMINAR REGISTRO DE MADRE    ")
    print("\n--------------------------------")

    madres = cargar_madres()
    if not madres:
        print("No existen madres registradas")
        return

    print("\n--- MADRES REGISTRADAS ---")
    for m in madres:
        print(f"Código: {m['codigo']} | Nombre: {m['nombres']} {m['paterno']} {m['materno']} | DNI: {m['dni']}")
    print("--------------------------")

    codigo = input("Ingrese el código de la madre a eliminar: ").strip().upper()

    for i in range(len(madres)):
        if madres[i]["codigo"].upper() == codigo:
            m = madres[i]
            print(f"\nRegistro seleccionado: {m['nombres']} {m['paterno']} {m['materno']} (DNI: {m['dni']})")
            confirmacion = input("¿Está seguro de eliminar este registro? (SI/NO): ").strip().upper()

            if confirmacion == "SI":
                madres.pop(i)
                guardar_madres(madres)
                print("\nRegistro de la madre eliminado correctamente")
            elif confirmacion == "NO":
                print("Eliminación cancelada.")
            else:
                print("Respuesta no válida/ No se eliminó el registro")
            return

    print("No se encontró ninguna madre con ese código")
