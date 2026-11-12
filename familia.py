import csv
import os

from padre import registrar_padre
from madre import registrar_madre
from estudiantes import registrar_estudiante

RUTA_CSV = "datos/familias.csv"
ENCABEZADOS = ["codigo_familia", "codigo_padre", "codigo_madre", "codigo_estudiante"]

def cargar_familias():
    lista = []
    if os.path.exists(RUTA_CSV):
        with open(RUTA_CSV, "r", newline="", encoding="utf-8-sig") as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                lista.append(fila)
    return lista

def guardar_familias(lista):
    os.makedirs("datos", exist_ok=True)
    with open(RUTA_CSV, "w", newline="", encoding="utf-8-sig") as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=ENCABEZADOS)
        escritor.writeheader()
        escritor.writerows(lista)

def generar_codigo_familia(lista):
    numero = len(lista) + 1
    return f"F{numero:03d}"

def registrar_familia():
    print("\n")
    print("  REGISTRO INTEGRAL DE FAMILIA - ESTUDIANTE ")
    
    familias = cargar_familias()
    
    cod_padre = registrar_padre()
    

    cod_madre = registrar_madre()
    

    cod_estudiante = registrar_estudiante()
    
   
    for f in familias:
        if f["codigo_estudiante"] == cod_estudiante:
            print(f"\nAviso: Este estudiante ya está vinculado al expediente familiar {f['codigo_familia']}.")
            return f["codigo_familia"]
            
    codigo_f = generar_codigo_familia(familias)
    
    nueva_familia = {
        "codigo_familia": codigo_f,
        "codigo_padre": cod_padre,
        "codigo_madre": cod_madre,
        "codigo_estudiante": cod_estudiante
    }
    
    familias.append(nueva_familia)
    guardar_familias(familias)
    
    print("\n")
    print("--- VÍNCULO FAMILIAR REGISTRADO ---")
    print(f"Código Familia:    {codigo_f}")
    print(f"Código Padre:      {cod_padre}")
    print(f"Código Madre:      {cod_madre}")
    print(f"Código Estudiante: {cod_estudiante}")
    print("Guardado en datos/familias.csv")
    
    
    return codigo_f

