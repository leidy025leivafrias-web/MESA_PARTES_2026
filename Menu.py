from Guardar_Expediente import (cargar_expedientes,cargar_calificaciones, guardar_solo_expedientes, guardar_solo_calificaciones)
from padre import registrar_padre
from madre import registrar_madre
from estudiantes import registrar_estudiante, cargar_estudiantes
from familia import registrar_familia
from padre import registrar_padre
from modificar_padre import modificar_padre
from eliminar_padre import eliminar_padre

from madre import registrar_madre
from modificar_madre import modificar_madre
from eliminar_madre import eliminar_madre

from estudiantes import registrar_estudiante, cargar_estudiantes
from modificar_estudiante import modificar_estudiante
from eliminar_estudiante import eliminar_estudiante

from familia import registrar_familia
from modificar_familia import modificar_familia
from eliminar_familia import eliminar_familia
#PASO 3
from Expedientes import Expedientes
from listar_expedientes import listado_expedientes
from buscar_expedientes import buscar_expedientes
from modificar_expediente import modificar_expediente
from eliminar_expediente import eliminar_expediente
#PASO 4
from registrar_calificaciones import registrar_calificaciones
from listar_calificaciones import listar_calificaciones
from buscar_calificaciones import buscar_calificaciones
from modificar_calificaciones import modificar_calificacion
from eliminar_calificaciones import eliminar_calificaciones

#PASO 5
from mostrar_calculos import mostrar_calculos
def mostrar_menu():
    print("\n++++++++++++++++++++++++++++++++++++++++++++++++")
    print("  MESA DE PARTES DIGITAL - FE Y ALEGRIA N° 37")
    print("++++++++++++++++++++++++++++++++++++++++++++++++")
    print("1. GESTIÓN DE PERSONAS")
    print("2. GESTIÓN DE FAMILIAS")
    print("3. GESTIÓN DE EXPEDIENTES")
    print("4. GESTIÓN DE CALIFICACIONES")
    print("5. CÁLCULOS ACADÉMICOS")
    print("6. GUARDAR INFORMACIÓN")
    print("7. SALIR")

    print("="*50)
    print("Seleccione una opción: ")

padres = []
madres = []
estudiantes = []
familias = []
expedientes = cargar_expedientes()
calificaciones = cargar_calificaciones()

def guardar_todo():
    guardar_solo_expedientes(expedientes)
    guardar_solo_calificaciones(calificaciones)

def main():
        global expedientes
        expedientes = cargar_expedientes()
        while True:
            mostrar_menu()
            opcion = input("> ")
            
            if opcion == '1':
                while True:
                    print("\n--- GESTIÓN DE PERSONAS ---")
                    print("1. Registrar Padre")
                    print("2. Registrar Madre")
                    print("3. Registrar Estudiante")
                    print("4. Modificar Persona")
                    print("5. Eliminar Persona")
                    print("6. Volver al Menu principal")
                    sub_opcion = input("Seleccione una opción: ").strip()
                    
                    if sub_opcion == '6':
                        break
                    elif sub_opcion == "1":
                        registrar_padre()
                    elif sub_opcion == '2':
                        registrar_madre()
                    elif sub_opcion == '3':
                        registrar_estudiante()
                    elif sub_opcion == "4":
                        print("¿Qué persona desea modificar?")
                        print("1. Padre | 2. Madre | 3. Estudiante")
                        op_mod = input("Elija (1-3): ").strip()
                        if op_mod == '1':
                            modificar_padre()
                        elif op_mod == '2':
                            modificar_madre()
                        elif op_mod == '3':
                            modificar_estudiante()
                        else:
                            print("Opción no válida.")
                    elif sub_opcion == '5':
                        print("\n¿Qué persona desea eliminar?")
                        print("1. Padre | 2. Madre | 3. Estudiante")
                        op_eli = input("Elija (1-3): ").strip()
                        if op_eli == '1':
                            eliminar_padre()
                        elif op_eli == '2':
                            eliminar_madre()
                        elif op_eli == '3':
                            eliminar_estudiante()
                        else:
                            print("Opción no válida.")
                    else:
                        print("Opción no válida.")
                        input("\nPresione enter para continuar...")

            elif opcion == "2":
                while True:
                    print("\n--- GESTIÓN DE FAMILIAS ---")
                    print("1. Registrar Familia")
                    print("2. Modificar Vínculo Familiar")
                    print("3. Eliminar Vínculo Familiar")
                    print("4. Volver al Menú Principal")
                    sub_fam = input("Seleccione una opción: ").strip()
                    
                    if sub_fam == '4':
                        break
                    elif sub_fam == '1':
                        registrar_familia()
                    elif sub_fam == '2':
                        modificar_familia()
                    elif sub_fam == '3':
                        eliminar_familia()
                    else:
                        print("Opción no válida.")
                    input("\nPresione enter para continuar...")

            elif opcion == "3":
                while True:
                    print("\n--- GESTIÓN DE EXPEDIENTES ---")
                    print("1. Registrar Expediente")
                    print("2. Listar Expedientes")
                    print("3. Buscar Expediente")
                    print("4. Modificar Expediente")
                    print("5. Eliminar Expediente")
                    print("6. Volver al Menú Principal")
                    sub_opcion_exp = input("Seleccione una opción: ").strip()
                    if sub_opcion_exp == "6":
                        break
                    estudiantes = cargar_estudiantes()

                    if sub_opcion_exp == "6":
                        break
                    estudiantes = cargar_estudiantes()

                    if sub_opcion_exp == '1':
                        Expedientes(expedientes, estudiantes)
                    elif sub_opcion_exp == '2':
                        listado_expedientes(expedientes)
                    elif sub_opcion_exp == '3':
                        buscar_expedientes(expedientes)
                    elif sub_opcion_exp == '4':
                        modificar_expediente(expedientes, estudiantes)
                    elif sub_opcion_exp == "5":
                        eliminar_expediente(expedientes)
                    else:
                        print("*Opción no válida.*")
                    input("\nPresione enter para continuar...")

            elif opcion == "4":
                 while True:
                    print("\n--- GESTIÓN DE CALIFICACIONES ---")
                    print("1. Registrar Calificación")
                    print("2. Listar Calificaciones")
                    print("3. Buscar Calificaciones")
                    print("4. Modificar Calificaciones")
                    print("5. Eliminar Calificaciones")
                    print("6. Volver al Menú Principal")
                    sub_opcion_cal = input("Seleccione una opción: ").strip()
                    if sub_opcion_cal == "6":
                     break
                    estudiantes = cargar_estudiantes()
                    
                    if sub_opcion_cal == "1":
                        registrar_calificaciones(calificaciones, expedientes)
                        input("\nPresione enter para continuar...")
                    elif sub_opcion_cal == "2":
                        listar_calificaciones(calificaciones)
                    elif sub_opcion_cal == "3":
                        buscar_calificaciones(calificaciones)
                    elif sub_opcion_cal == "4":
                        modificar_calificacion(calificaciones)
                    elif sub_opcion_cal == "5":
                        eliminar_calificaciones(calificaciones)
                    else:
                       print("*Opción no válida.*")
                       input("\nPresione enter para continuar...")
            elif opcion == "5":
                mostrar_calculos (calificaciones)
                input("\nPresione enter para continuar...")

            elif opcion == "6":
                print("\n--- GUARDAR INFORMACIÓN ---")
                guardar_todo()
                print("¡Información guardada manualmente con éxito!")
                input("\nPresione enter para continuar...")

            elif opcion == "7":
                print("\n ----- GUARDANDO CAMBIOS Y SALIENDO -----")
                guardar_todo()
                print("¡Datos respaldados con éxito! Saliendo del sistema...")
                break





if __name__ == "__main__":
    main()