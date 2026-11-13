import csv
import os

def leer_csv(ruta):
    lista = []
    if os.path.exists(ruta):
        with open(ruta, "r", newline="", encoding="utf-8-sig") as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                lista.append(fila)
    return lista

def cargar_expedientes():
    print("\n--- CARGANDO REGISTROS DEL SISTEMA ---")
    datos = {
        "padres": leer_csv("datos/padres.csv"),
        "madres": leer_csv("datos/madres.csv"),
        "estudiantes": leer_csv("datos/estudiantes.csv"),
        "familias": leer_csv("datos/familias.csv"),
        "expedientes": leer_csv("datos/expedientes.csv"),
        "calificaciones": leer_csv("datos/calificaciones.csv")
    }
    print("Información cargada correctamente.")
    return datos
