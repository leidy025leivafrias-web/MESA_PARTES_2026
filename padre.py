import csv
import os

RUTA_CSV = "datos/padres.csv"
ENCABEZADOS = ["codigo", "dni", "nombres", "paterno", "materno", "telefono", "correo"]

def cargar_padres():
    lista = []
    if os.path.exists(RUTA_CSV):
        with open(RUTA_CSV, "r", newline="", encoding="utf-8-sig") as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                lista.append(fila)
    return lista

def guardar_padres(lista):
    os.makedirs("datos", exist_ok=True)
    with open(RUTA_CSV, "w", newline="", encoding="utf-8-sig") as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=ENCABEZADOS)
        escritor.writeheader()
        escritor.writerows(lista)

def generar_codigo_padre(lista):
    numero = len(lista) + 1
    return f"P{numero:03d}"

def validar_texto(mensaje):
    while True:
        texto = input(mensaje).strip()
        sin_espacios = texto.replace(" ", "")
        if len(sin_espacios) > 0 and sin_espacios.isalpha():
            return texto.title()
        print("Error: ingrese solo letras.")

def validar_dni():
    while True:
        dni = input("DNI del padre: ").strip()
        if len(dni) == 8 and dni.isdigit():
            return dni
        print("Error: el DNI debe tener 8 números.")

def validar_telefono():
    while True:
        telefono = input("Teléfono celular: ").strip()
        if len(telefono) == 9 and telefono.isdigit() and telefono.startswith("9"):
            return telefono
        print("Error: debe empezar con 9 y tener 9 dígitos.")

def validar_correo():
    while True:
        correo = input("Correo electrónico: ").strip()
        if "@" in correo and "." in correo and " " not in correo:
            return correo.lower()
        print("Error: ingrese un correo válido.")

def registrar_padre():
    print("\n--- REGISTRO DE PADRE ---")
    padres = cargar_padres()
    dni = validar_dni()
    
    for p in padres:
        if p["dni"] == dni:
            print(f"Padre ya registrado. Código: {p['codigo']}")
            return p["codigo"]
            
    nombres = validar_texto("Nombres: ")
    paterno = validar_texto("Apellido paterno: ")
    materno = validar_texto("Apellido materno: ")
    telefono = validar_telefono()
    correo = validar_correo()
    
    codigo = generar_codigo_padre(padres)
    
    nuevo_padre = {
        "codigo": codigo,
        "dni": dni,
        "nombres": nombres,
        "paterno": paterno,
        "materno": materno,
        "telefono": telefono,
        "correo": correo
    }
    
    padres.append(nuevo_padre)
    guardar_padres(padres)
    
    print("\n--- RESUMEN DEL REGISTRO ---")
    print(f"Código asignado: {codigo}")
    print(f"Nombre completo: {nombres} {paterno} {materno}")
    print("Guardado en datos/padres.csv")
    
    return codigo

