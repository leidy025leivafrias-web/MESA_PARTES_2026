def buscar_expedientes(expedientes):
    print("\n===================================")
    print("       BUSCAR EXPEDIENTE")
    print("===================================")

    if not expedientes:
        print("No existen expedientes registrados.")
        return

    codigo_buscado = input("Ingrese el código del expediente: ").strip().upper()
    expediente_encontrado = None

    for expediente in expedientes:
        if expediente.get("codigo", "").strip().upper() == codigo_buscado:
            expediente_encontrado = expediente
            break
        if expediente_encontrado is None:
            print("\nERROR: No se encontró ningún expediente con ese código.")
            return None

    print("\n========================================")
    print("       EXPEDIENTE ENCONTRADO")
    print("========================================")
    print(f"CÓDIGO: {expediente_encontrado['codigo']}")
    print(f"CÓDIGO DEL ESTUDIANTE: {expediente_encontrado['codigo_estudiante']}")
    print(f"NIVEL EDUCATIVO: {expediente_encontrado['nivel']}")
    print("========================================")
    
    return expediente_encontrado