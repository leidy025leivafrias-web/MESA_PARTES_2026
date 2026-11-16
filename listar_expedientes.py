from Guardar_Expediente import cargar_csv
def mostrar_datos(titulo, datos):
      
    print("\n===================================")
    print(f"       {titulo}")
    print("===================================")

    if not datos:
        print("No hay información registrada.")
        return
    for campo, valor in datos.items():
        print(f"{campo.replace('_', ' ').upper()}: {valor}")

def listado_expedientes(expedientes):
    if not expedientes:
        print("No hay expedientes para mostrar.")
        return
    
    estudiantes = cargar_csv("datos/estudiantes.csv")
    padres = cargar_csv("datos/padres.csv")
    madres = cargar_csv("datos/madres.csv")
    familias = cargar_csv("datos/familias.csv")
    calificaciones = cargar_csv("datos/calificaciones.csv")


    print("\n===================================")
    print("       LISTADO DE EXPEDIENTES")
    print("===================================")

    for numero, expediente in enumerate(expedientes,start=1):

        codigo_estudiante = expediente.get("codigo_estudiante", "").strip().upper()
        estudiante = next(
            (e for e in estudiantes if e.get("codigo")== codigo_estudiante),
            None
        )

        if estudiante:
            nombre = (
            estudiante.get("nombres", "") + " " +
            estudiante.get("paterno", "") + " " +
            estudiante.get("materno", "")
        )
        else:
            nombre = "Estudiante no encontrado"

    print(
        f"{numero}. {expediente.get('codigo')} "
        f"- {nombre.strip()} ({codigo_estudiante})"
    )
    
    try:
        seleccion = int(input("\nSeleccione un expediente: "))

        if seleccion < 1 or seleccion > len(expedientes):
            print("\nNúmero de expediente no válido.")
            return

    except ValueError:
        print("\nDebe ingresar un número.")
        return

    expediente = expedientes[seleccion - 1]
    codigo_estudiante = expediente.get("codigo_estudiante")
    codigo_expediente = expediente.get("codigo")

    estudiante = next(
        (e for e in estudiantes
         if e.get("codigo", "").strip().upper() ==
         str(codigo_estudiante).strip().upper()),
        None
    )

    familia = next(
    (f for f in familias
     if f.get("codigo_estudiante", "").strip().upper() ==
     str(codigo_estudiante).strip().upper()),
    None
    )

    padre = None
    madre = None

    if familia:
        codigo_padre = familia.get("codigo_padre")
        codigo_madre = familia.get("codigo_madre")

        padre = next(
            (p for p in padres if p.get("codigo") == codigo_padre),
            None
        )

        madre = next(
            (m for m in madres if m.get("codigo") == codigo_madre),
            None
        )

    notas = next(
        (c for c in calificaciones
         if c.get("codigo_expediente") == codigo_expediente),
        None
    )

    print("\n\n****************************************")
    print("       EXPEDIENTE COMPLETO")
    print("****************************************")

    mostrar_datos("DATOS DEL EXPEDIENTE", expediente)
    mostrar_datos("DATOS DEL ESTUDIANTE", estudiante)
    mostrar_datos("DATOS DEL PADRE", padre)
    mostrar_datos("DATOS DE LA MADRE", madre)
    mostrar_datos("CALIFICACIONES", notas)
