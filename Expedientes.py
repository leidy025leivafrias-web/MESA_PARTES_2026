from Codigo_expediente import Codigo_expediente
from Codigo_estudiante import Codigo_estudiante
from nivel_educativo import nivel_educativo

def Expedientes(expedientes, estudiantes=None):
    print("\n===================================")
    print("      REGISTRAR EXPEDIENTE")
    print("===================================")

    codigo = Codigo_expediente(expedientes)
    print(f"\nCODIGO GENERADO: {codigo}")

    codigo_estudiante = Codigo_estudiante(estudiantes)

    for expediente in expedientes:
        if expediente["codigo_estudiante"] == codigo_estudiante:
            print("*Error: este estudiante ya tiene un expediente registrado.*")
            return

    nivel = nivel_educativo()

    expediente = {
        "codigo": codigo,
        "codigo_estudiante": codigo_estudiante,
        "nivel": nivel,
        "estado": "Pendiente"
    }

    expedientes.append(expediente)

    print("\nExpediente registrado correctamente.")
    print(f"Código del expediente: {codigo}")