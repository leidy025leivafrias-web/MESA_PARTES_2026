from madre import cargar_madres, guardar_madres, validar_dni, validar_texto, validar_telefono, validar_correo

def modificar_madre():
    print("\n--------------------------------")
    print("    MODIFICAR DATOS DE LA MADRE   ")
    print("\n--------------------------------")

    madres = cargar_madres()
    if not madres:
        print("")
        return

    print("\n--- MADRES REGISTRADAS ---")
    for m in madres:
        print(f"Código: {m['codigo']} | Nombre: {m['nombres']} {m['paterno']} {m['materno']} | DNI: {m['dni']}")
    print("--------------------------")

    codigo = input("Ingrese el código de la madre a modificar: ").strip().upper()

    for m in madres:
        if m["codigo"].upper() == codigo:
            print(f"\nEditando registro de: {m['nombres']} {m['paterno']} {m['materno']}")
            print("Ingrese los nuevos datos:")

            nuevo_dni = validar_dni()
            for otra in madres:
                if otra["dni"] == nuevo_dni and otra["codigo"].upper() != codigo:
                    print(f"Error: ese DNI ya está registrado con el código {otra['codigo']}")
                    return

            m["dni"] = nuevo_dni
            m["nombres"] = validar_texto("Nuevos nombres: ")
            m["paterno"] = validar_texto("Nuevo apellido paterno: ")
            m["materno"] = validar_texto("Nuevo apellido materno: ")
            m["telefono"] = validar_telefono()
            m["correo"] = validar_correo()

            guardar_madres(madres)
            print("\nTodos los datos de la madre fueron actualizados correctamente")
            return

    print("No se encontró ninguna madre con ese código")
