from calcular_promedio import calcular_promedio
from nota_maxima import nota_maxima
from nota_minima import nota_minima
from condicion_estudiante import determinar_condicion
def mostrar_calculos(calificaciones):
    if len(calificaciones) == 0:
        print("*No hay calificaciones registradas.*")
        return

    for calificacion in calificaciones:
        promedio = calcular_promedio(calificaciones)
        maxima = nota_maxima(calificaciones)
        minima = nota_minima(calificaciones)
        condicion = determinar_condicion(calificaciones)

        print("-" * 50)
        print("EXPEDIENTE:", calificacion["codigo_expediente"])
        print(f"PROMEDIO: {promedio:.2f}")
        print(f"NOTA MÁXIMA: {maxima:.2f}")
        print(f"NOTA MÍNIMA: {minima:.2f}")
        print("CONDICIÓN:", condicion)