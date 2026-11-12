import csv
import os

RUTA_CSV = "datos/estudiantes.csv"
ENCABEZADOS = ["codigo", "dni", "nombres", "paterno", "materno", "nivel", "turno", "taller"]

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
        print("Error: ingrese solo letras")

def validar_dni():
    while True:
        dni = input("DNI del estudiante: ").strip()
        if len(dni) == 8 and dni.isdigit():
            return dni
        print("Error: el DNI debe tener 8 números")

def validar_nivel():
    while True:
        print("\nNiveles educativos: ")
        print("1. Inicial (5 años)")
        print("2. Primaria")
        print("3. Secundaria")
        print("4. Especial (EBE 4 - 17 años)")
        opcion = input("Seleccione el nivel (1 - 4): ").strip()

        if opcion == "1":
            return "Inicial"
        elif opcion == "2":
            return "Primaria"
        elif opcion == "3":
            return "Secundaria"
        elif opcion == "4":
            return "Especial (EBE)"
        print("Error: elija una opción válida (1 al 4)")

def validar_turno():
    while True:
        print("Turnos: 1. Mañana   2. Tarde")
        opcion = input("Seleccione el turno (1-2): ").strip()
        if opcion == "1":
            return "Mañana"
        elif opcion == "2":
            return "Tarde"
        print("Error: elija 1 o 2")

def validar_taller():
    while True:
        print("\nTalleres técnicos de Secundaria:")
        print("1. Ofimática  2. Carpintería  3. Electrónica   4. Corte y confección")
        opcion = input("Seleccione el taller (1-4): ").strip()
        
        if opcion == "1":
            return "Ofimática"
        elif opcion == "2":
            return "Carpintería"
        elif opcion == "3":
            return "Electrónica"
        elif opcion == "4":
            return "Corte y Confección"
        print("Error: elija del 1 al 4")


def registrar_estudiante():
    print("\n--- REGISTRO DE ESTUDIANTE ---")
    estudiantes = cargar_estudiantes()
    dni = validar_dni()
    
    for e in estudiantes:
        if e["dni"] == dni:
            print(f"Estudiante ya registrado - Código: {e['codigo']}")
            return e["codigo"]
            
    nombres = validar_texto("Nombres: ")
    paterno = validar_texto("Apellido paterno: ")
    materno = validar_texto("Apellido materno: ")
    nivel = validar_nivel()
    turno = validar_turno()

    if nivel == "Secundaria":
        taller = validar_taller()
    else:
        taller = "No aplica"
    
    codigo = generar_codigo_estudiante(estudiantes)
    
    nuevo_estudiante = {
        "codigo": codigo,
        "dni": dni,
        "nombres": nombres,
        "paterno": paterno,
        "materno": materno,
        "nivel": nivel,
        "turno": turno,
        "taller": taller
    }
    
    estudiantes.append(nuevo_estudiante)
    guardar_estudiantes(estudiantes)
    
    print("\n--- RESUMEN DEL REGISTRO ---")
    print(f"Código asignado: {codigo}")
    print(f"Estudiante: {nombres} {paterno} {materno}")
    print(f"Nivel y Turno: {nivel} - Turno {turno}")
    if taller != "No aplica":
        print(f"Taller técnico: {taller}")
    print("\n Guardado en datos/estudiantes.csv")
    
    return codigo
