from familia import cargar_familias, guardar_familias
from padre import cargar_padres
from madre import cargar_madres
from estudiantes import cargar_estudiantes

def existe_codigo(lista, codigo):
    for item in lista:
        if item["codigo"].upper() == codigo:
            return True
    return False

def modificar_familia():
    print("\n------------------------------------------")
    print("       MODIFICAR VÍNCULO FAMILIAR         ")
    print("------------------------------------------")
    
    familias = cargar_familias()
    if not familias:
        print("No existen familias registradas")
        return

    print("\n--- FAMILIAS REGISTRADAS ---")
    for f in familias:
        print(f"Familia: {f['codigo_familia']} | Padre: {f['codigo_padre']} | Madre: {f['codigo_madre']} | Estudiante: {f['codigo_estudiante']}")
    print("----------------------------")

    codigo = input("Ingrese el código de familia a modificar: ").strip().upper()
    
    for f in familias:
        if f["codigo_familia"].upper() == codigo:
            print(f"\nEditando vínculo {codigo}:")
            padres = cargar_padres()
            madres = cargar_madres()
            estudiantes = cargar_estudiantes()
            
            nuevo_padre = input(f"Nuevo código de padre ({f['codigo_padre']}): ").strip().upper()
            if not existe_codigo(padres, nuevo_padre):
                print("Error: ese código de padre no existe en el sistema.")
                return
                
            nueva_madre = input(f"Nuevo código de madre ({f['codigo_madre']}): ").strip().upper()
            if not existe_codigo(madres, nueva_madre):
                print("Error: ese código de madre no existe en el sistema")
                return
                
            nuevo_est = input(f"Nuevo código de estudiante ({f['codigo_estudiante']}): ").strip().upper()
            if not existe_codigo(estudiantes, nuevo_est):
                print("Error: ese código de estudiante no existe en el sistema")
                return
                
            f["codigo_padre"] = nuevo_padre
            f["codigo_madre"] = nueva_madre
            f["codigo_estudiante"] = nuevo_est
            
            guardar_familias(familias)
            print("\nVínculo familiar actualizado correctamente")
            return
            
    print("No se encontró ninguna familia con ese código")
