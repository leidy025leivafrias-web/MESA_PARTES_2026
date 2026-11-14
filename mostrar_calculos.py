from calcular_promedio import calcular_promedio
from nota_maxima import nota_maxima
from nota_minima import nota_minima
from condicion_estudiante import determinar_condicion

def mostrar_calculos(calificaciones):
    if len(calificaciones) == 0:
        print("\n*No hay calificaciones registradas.*")
        return

    for calificacion in calificaciones:
        promedio = calcular_promedio(calificacion)
        maxima = nota_maxima(calificacion)
        minima = nota_minima(calificacion)
        condicion = determinar_condicion(promedio)

        print("-" * 50)
        print("EXPEDIENTE:", calificacion.get("codigo_expediente", "N/A"))
        print(f"PROMEDIO: {promedio:.2f}")
        print(f"NOTA MÁXIMA: {maxima:.2f}")
        print(f"NOTA MÍNIMA: {minima:.2f}")
        print("CONDICIÓN:", condicion)
        print("-" * 50)