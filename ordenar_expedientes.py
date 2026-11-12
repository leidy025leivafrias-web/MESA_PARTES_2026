def ordenar_expedientes_por_codigo(expedientes):
    print("\n--- ORDENAR EXPEDIENTES POR CÓDIGO ---")
    
    total = len(expedientes)
    
    if total == 0:
        print("No hay expedientes registrados para ordenar.")
        return

    for i in range(total):
        for j in range(0, total - i - 1):
            
      
            if expedientes[j]["codigo"] > expedientes[j + 1]["codigo"]:
                
                aux_expediente = expedientes[j]
                expedientes[j] = expedientes[j + 1]
                expedientes[j + 1] = aux_expediente

    print("¡Éxito! Todos los expedientes han sido ordenados por su código.")