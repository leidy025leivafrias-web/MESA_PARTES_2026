
from Codigo_expediente import Codigo_expediente
def Expedientes(expedientes, estudiantes):
    print("\n===================================")
    print("      REGISTRAR EXPEDIENTE")
    print("===================================")

    if not estudiantes:
        print("\nNo hay estudiantes registrados.")
        return
    
    codigo_estudiante = input("\nIngrese el código del estudiante: ").strip().upper()
    estudiante_encontrado = None

    for estudiante in estudiantes:
        if estudiante.get("codigo", "").strip().upper() == codigo_estudiante:
            estudiante_encontrado = estudiante
            break

    if estudiante_encontrado is None:
        print("\nERROR: No se encontró al estudiante.")
        return

    for expediente in expedientes:
        if expediente["codigo_estudiante"] == codigo_estudiante:
            print("\nERROR: El estudiante ya tiene un expediente registrado.")
            return

    codigo = Codigo_expediente(expedientes)

    nivel = estudiante_encontrado.get("nivel", "No especificado")

    nuevo_expediente = {
        "codigo": codigo,
        "codigo_estudiante": codigo_estudiante,
        "nivel": nivel,
    }

    expedientes.append(nuevo_expediente)

    print("\n========================================")
    print("       EXPEDIENTE REGISTRADO")
    print("========================================")
    print(f"CÓDIGO DEL EXPEDIENTE: {codigo}")
    print(f"CÓDIGO DEL ESTUDIANTE: {codigo_estudiante}")
    print(f"NIVEL EDUCATIVO: {nivel}")
    print("========================================")