import csv
import os

def escribir_csv(ruta, encabezados, lista):
    os.makedirs("datos", exist_ok=True)
    campos = ["codigo", "codigo_estudiante", "nivel", "estado"]
    with open(ruta, "w", newline="", encoding="utf-8-sig") as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=encabezados)
        escritor.writeheader()
        escritor.writerows(lista)

def guardar_expedientes(padres, madres, estudiantes, familias, expedientes, calificaciones):
    print("\n--- GUARDANDO TODOS LOS REGISTROS EN CSV ---")
    
    escribir_csv("datos/padres.csv", ["codigo", "dni", "nombres", "paterno", "materno", "telefono", "correo"], padres)
    escribir_csv("datos/madres.csv", ["codigo", "dni", "nombres", "paterno", "materno", "telefono", "correo"], madres)
    escribir_csv("datos/estudiantes.csv", ["codigo", "dni", "nombres", "paterno", "materno", "nivel", "turno", "taller"], estudiantes)
    escribir_csv("datos/familias.csv", ["codigo_familia", "codigo_padre", "codigo_madre", "codigo_estudiante"], familias)
    
    if len(expedientes) > 0:
        encabezados_exp = list(expedientes[0].keys())
        escribir_csv("datos/expedientes.csv", encabezados_exp, expedientes)
        
    if len(calificaciones) > 0:
        encabezados_cal = list(calificaciones[0].keys())
        escribir_csv("datos/calificaciones.csv", encabezados_cal, calificaciones)
        
    print("¡Respaldo exitoso! Todos los registros fueron guardados en la carpeta 'datos/'")
    print("\n")

def cargar_csv(ruta):
    lista = []
    if not os.path.exists(ruta):
        return lista
    try:
        with open(ruta, mode="r", encoding="utf-8-sig") as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                lista.append(fila)
    except Exception as e:
        print(f"Error al cargar {ruta}: {e}")
    return lista

def cargar_expedientes():
    return cargar_csv("datos/expedientes.csv")

def cargar_calificaciones():
    lista = cargar_csv("datos/calificaciones.csv")
    for registro in lista:
        for clave in ("bimestre1", "bimestre2", "bimestre3", "bimestre4"):
            registro[clave] = float(registro[clave])
    return lista

def guardar_solo_expedientes(expedientes):
    os.makedirs("datos", exist_ok=True)

    encabezados= ["codigo", "codigo_estudiante", "nivel", "estado"]
    escribir_csv("datos/expedientes.csv", encabezados, expedientes)
    print("\nExpediente guardado automáticamente en el CSV.")

def guardar_solo_calificaciones(calificaciones):
    encabezados_cal = ["codigo_expediente", "bimestre1", "bimestre2", "bimestre3", "bimestre4"]
    escribir_csv("datos/calificaciones.csv", encabezados_cal, calificaciones)
