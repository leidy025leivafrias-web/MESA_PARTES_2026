import csv
import os

RUTA_CSV = "datos/estudiantes.csv"
ENCABEZADOS = ["codigo", "dni", "nombres", "paterno", "materno", "nivel"]

def cargar_estudiantes():
    lista = []
    if os.path.exists(RUTA_CSV):
        with open(RUTA_CSV, "r", newline="", encoding="utf-8-sig") as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                lista.append(fila)
    return lista

def guardar_estudiantes(lista):
    os.makedirs("datos", exist_ok=True)
    with open(RUTA_CSV, "w", newline="", encoding="utf-8-sig") as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=ENCABEZADOS)
        escritor.writeheader()
        escritor.writerows(lista)

def generar_codigo_estudiante(lista):
    numero = len(lista) + 1
    return f"E{numero:03d}"

def validar_texto(mensaje):
    while True:
        texto = input(mensaje).strip()
        sin_espacios = texto.replace(" ", "")
        if len(sin_espacios) > 0 and sin_espacios.isalpha():
            return texto.title()
        print("Error: ingrese solo letras.")

def validar_dni():
    while True:
        dni = input("DNI del estudiante: ").strip()
        if len(dni) == 8 and dni.isdigit():
            return dni
        print("Error: el DNI debe tener 8 números.")

def validar_nivel():
    while True:
        print("\nNiveles: 1. Inicial  2. Primaria  3. Secundaria")
        opcion = input("Seleccione el nivel educativo (1-3): ").strip()
        if opcion == "1":
            return "Inicial"
        elif opcion == "2":
            return "Primaria"
        elif opcion == "3":
            return "Secundaria"
        print("Error: elija una opción válida (1, 2 o 3)")

def registrar_estudiante():
    print("\n--- REGISTRO DE ESTUDIANTE ---")
    estudiantes = cargar_estudiantes()
    dni = validar_dni()
    
    for e in estudiantes:
        if e["dni"] == dni:
            print(f"Estudiante ya registrado. Código: {e['codigo']}")
            return e["codigo"]
            
    nombres = validar_texto("Nombres: ")
    paterno = validar_texto("Apellido paterno: ")
    materno = validar_texto("Apellido materno: ")
    nivel = validar_nivel()
    
    codigo = generar_codigo_estudiante(estudiantes)
    
    nuevo_estudiante = {
        "codigo": codigo,
        "dni": dni,
        "nombres": nombres,
        "paterno": paterno,
        "materno": materno,
        "nivel": nivel
    }
    
    estudiantes.append(nuevo_estudiante)
    guardar_estudiantes(estudiantes)
    
    print("\n--- RESUMEN DEL REGISTRO ---")
    print(f"Código asignado: {codigo}")
    print(f"Nombre completo: {nombres} {paterno} {materno}")
    print(f"Nivel educativo: {nivel}")
    print("\n Guardado en datos/estudiantes.csv")
    
    return codigo
#preuba temporal
registrar_estudiante()
