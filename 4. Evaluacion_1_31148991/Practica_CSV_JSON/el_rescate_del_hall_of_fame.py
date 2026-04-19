"""
ENUNCIADO:
Como arquitectos de software, han recibido un "archivador" (partidas_gamers.csv) 
con datos de una competencia regional. Su misión es extraer la información 
de la "PC Master Race" (solo registros de la consola PC) y generar un reporte 
de alto nivel para el patrocinador en formato JSON.

REQUERIMIENTOS TÉCNICOS:
1. Lectura: Usar 'with' y 'csv.reader'. Saltar el encabezado.
2. Filtrado: Procesar solo registros donde la consola sea "PC".
3. Blindaje: Usar bloque try-except para convertir el puntaje a entero (int). 
    Si el dato es corrupto, imprimir el error y continuar con el siguiente registro.
4. Cálculos: 
    - Determinar el puntaje más alto entre los jugadores de PC.
    - Calcular el promedio de tiempo jugado de los registros procesados con éxito.
5. Persistencia: Exportar los resultados a 'hall_of_fame.json' con la estructura
    de metadatos y estadísticas solicitada.
"""

# Importar las librerías necesarias
import csv
import json

# Desarrollar la lógica a partir de aquí:
def procesar_partidas_pc():
    max_puntaje = 0
    suma_tiempo = 0
    registros_validos = 0
    
    with open('partidas_gamers.csv', mode = 'r', encoding = 'utf-8') as archivo_csv:
        lector = csv.reader(archivo_csv)
        next(lector, None)
        
        for fila in lector:
            if len(fila) >= 5:
                jugador = fila[0]
                consola = fila[1]
                puntaje_str = fila[3]
                tiempo_str = fila[4]
                
                if consola == "PC":
                    try:
                        puntaje = int(puntaje_str)
                        tiempo = int(tiempo_str)
                        
                        if puntaje > max_puntaje:
                            max_puntaje = puntaje
                        suma_tiempo = suma_tiempo + tiempo
                        registros_validos = registros_validos + 1

                    except ValueError:
                        print("Error: El jugador", jugador, "tiene datos corruptos.")
                        continue
    if registros_validos > 0:
        promedio_tiempo = suma_tiempo / registros_validos
    else:
        promedio_tiempo = 0.0        
    return max_puntaje, promedio_tiempo, registros_validos

def generar_reporte(max_puntaje, promedio_tiempo, registros_validos):
    diccionario_metadatos = {}
    diccionario_metadatos["proyecto"] = "El rescate del Hall of Fame"
    diccionario_metadatos["plataforma_objetivo"] = "PC Master Race"
    diccionario_metadatos["registros_exitosos_procesados"] = registros_validos
    
    diccionario_estadisticas = {}
    diccionario_estadisticas["puntaje_mas_alto"] = max_puntaje
    diccionario_estadisticas["promedio_tiempo_jugado_min"] = round(promedio_tiempo, 2)
    
    reporte_final = {}
    reporte_final["metadatos"] = diccionario_metadatos
    reporte_final["estadisticas"] = diccionario_estadisticas
    
    with open('hall_of_fame.json', mode = 'w', encoding = 'utf-8') as archivo_json:
        json.dump(reporte_final, archivo_json, indent=4)

if __name__ == "__main__":
    print("Iniciando escaneo de partidas...")    
    puntaje_max, prom_tiempo, total_registros = procesar_partidas_pc()

    if total_registros > 0:
        generar_reporte(puntaje_max, prom_tiempo, total_registros)
        print("Reporte generado exitosamente.")
    else:
        print("No hay registros.")