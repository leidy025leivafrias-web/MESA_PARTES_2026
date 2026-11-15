from padre import cargar_padres, guardar_padres, validar_dni, validar_texto, validar_telefono, validar_correo

def modificar_padre():
    print("\n--------------------------------")
    print("     MODIFICAR DATOS DEL PADRE    ")
    print("\n--------------------------------")
    
    padres = cargar_padres()
    if not padres:
        print("No existen padres registrados")
        return

    print("\n--- PADRES REGISTRADOS ---")
    for p in padres:
        print(f"Código: {p['codigo']} | Nombre: {p['nombres']} {p['paterno']} {p['materno']} | DNI: {p['dni']}")
    print("--------------------------")

    codigo = input("Ingrese el código del padre a modificar: ").strip().upper()
    
    for p in padres:
        if p["codigo"].upper() == codigo:
            print(f"Editando registro de: {p['nombres']} {p['paterno']} {p['materno']}")
            print("\nIngrese los nuevos datos:")
            
            nuevo_dni = validar_dni()
            for otro in padres:
                if otro["dni"] == nuevo_dni and otro["codigo"].upper() != codigo:
                    print(f"Error: ese DNI ya está registrado con el código {otro['codigo']}")
                    return
                    
            p["dni"] = nuevo_dni
            p["nombres"] = validar_texto("Nuevos nombres: ")
            p["paterno"] = validar_texto("Nuevo apellido paterno: ")
            p["materno"] = validar_texto("Nuevo apellido materno: ")
            p["telefono"] = validar_telefono()
            p["correo"] = validar_correo()
            
            guardar_padres(padres)
            print("\nTodos los datos del padre fueron actualizados correctamente")
            return
            
    print("No se encontró ningún padre con ese código")

