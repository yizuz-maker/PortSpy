from listas.operaciones_listas import obtener_puertos_abiertos, contar_puertos_abiertos, ordenar_por_puerto
from cadenas.strings_utils import limpiar_ip, obtener_prefix
from diccionarios.estructura_datos import construir_escaneos_por_ip
from matrices.operaciones_matriz import crear_matriz
import io
import sys

"""
Presenta por consola la información estructurada de escaneos de múltiples hosts,
y también retorna el resultado como un string.

Redirige temporalmente la salida estándar (`sys.stdout`) a un buffer para capturar
toda la información mostrada y luego restaurar la salida original.

@param matriz_general Lista de matrices de resultados, donde cada matriz contiene
       filas con el formato [ip, puerto, estado, banner].

@return Un string con todo el contenido que fue impreso por consola.
"""
def presentador_consola(matriz_general):
    buffer = io.StringIO()
    stdout_original = sys.stdout
    sys.stdout = buffer
    try:
        for matriz in matriz_general:
            ip = matriz[0][0]
            abiertos = obtener_puertos_abiertos(matriz)
            total_abiertos = contar_puertos_abiertos(matriz)
            matriz_ordenada = ordenar_por_puerto(matriz)

            print("\nMatriz ordenada por número de puerto:")
            for fila in matriz_ordenada:
                if fila[2] == 'abierto':
                    print(f"{fila[0]:<15} {fila[1]:<10} {fila[2]:<10} {fila[3]:<10}")

            print(f"\nPrefijo de la red: {obtener_prefix(ip)}")
            print(f"\nPuertos abiertos detectados: {abiertos}")
            print(f"Cantidad total de puertos abiertos: {total_abiertos}")
            print("\nResumen estructurado:")

            print(f"{ip}")
            for ip, puerto, estado, banner in matriz:
                print(f"   Puerto {puerto}: {estado} {banner}")
    finally:
        sys.stdout = stdout_original

    resultado = buffer.getvalue()
    print(resultado)

    return resultado

