from estudiantes import cargar_estudiantes, guardar_estudiantes, validar_dni, validar_texto, validar_nivel, validar_turno, validar_taller

def modificar_estudiante():
    print("\n----------------------------------------")
    print("      MODIFICAR DATOS DEL ESTUDIANTE      ")
    print("------------------------------------------")
    
    estudiantes = cargar_estudiantes()
    if not estudiantes:
        print("No existen estudiantes registrados.")
        return

    print("\n--- ESTUDIANTES REGISTRADOS ---")
    for e in estudiantes:
        print(f"Código: {e['codigo']} | Nombre: {e['nombres']} {e['paterno']} {e['materno']} | Nivel: {e['nivel']} ({e['turno']})")
    print("-------------------------------")

    codigo = input("Ingrese el código del estudiante a modificar: ").strip().upper()
    
    for e in estudiantes:
        if e["codigo"].upper() == codigo:
            print(f"\nEditando registro de: {e['nombres']} {e['paterno']} {e['materno']}")
            print("Ingrese los nuevos datos:")
            
            nuevo_dni = validar_dni()
            for otro in estudiantes:
                if otro["dni"] == nuevo_dni and otro["codigo"].upper() != codigo:
                    print(f"Error: ese DNI ya está registrado con el código {otro['codigo']}.")
                    return
                    
            e["dni"] = nuevo_dni
            e["nombres"] = validar_texto("Nuevos nombres: ")
            e["paterno"] = validar_texto("Nuevo apellido paterno: ")
            e["materno"] = validar_texto("Nuevo apellido materno: ")
            e["nivel"] = validar_nivel()
            e["turno"] = validar_turno()
            
            if e["nivel"] == "Secundaria":
                e["taller"] = validar_taller()
            else:
                e["taller"] = "No aplica"
            
            guardar_estudiantes(estudiantes)
            print("\nTodos los datos del estudiante fueron actualizados correctamente")
            return
            
    print("No se encontró ningún estudiante con ese código")
