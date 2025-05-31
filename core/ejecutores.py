from scanner.network_scanner import escanear_hosts, escanear_puertos
from matrices.operaciones_matriz import crear_matriz, mostrar_matriz
from listas.operaciones_listas import obtener_puertos_abiertos, contar_puertos_abiertos, ordenar_por_puerto
from cadenas.strings_utils import limpiar_ip, obtener_prefix
from diccionarios.estructura_datos import construir_escaneos_por_ip
from archivos.leer_ips import leer_ips_desde_txt
import json

def procesar_host_unico(ip, puertos, threads):
    ip = limpiar_ip(ip)
    resultados = escanear_puertos(ip, puertos, threads)
    escaneos_por_ip = construir_escaneos_por_ip(ip, resultados)

    matriz = crear_matriz(ip, resultados)
    abiertos = obtener_puertos_abiertos(matriz)
    total_abiertos = contar_puertos_abiertos(matriz)
    matriz_ordenada = ordenar_por_puerto(matriz)

    print(f"\nPuertos abiertos detectados: {abiertos}")
    print(f"Cantidad total de puertos abiertos: {total_abiertos}")

    print("\nMatriz ordenada por número de puerto:")
    for fila in matriz_ordenada:
        if fila[2] == 'abierto':
            print(f"{fila[0]:<15} {fila[1]:<10} {fila[2]:<10} {fila[3]:<10}")

    print(f"\nPrefijo de la red: {obtener_prefix(ip)}")
    print("\nResumen estructurado:")
    for ip, datos in escaneos_por_ip.items():
        print(f"{ip}: ")
        for puerto in datos:
            print(f"  Puerto {puerto['puerto']}: {puerto['estado']} {puerto['banner']}")


def procesar_multiples_hosts(archivo, puertos, threads):
    hosts = leer_ips_desde_txt(archivo)
    resultados = escanear_hosts(hosts, puertos, threads)
 
    print("Hosts: ",hosts)
    print("Resultado: ",resultados)
    print(json.dumps(resultados, indent=4, ensure_ascii=False)) # Printear los resultados en forma de json (paso previo a dumpear en un archivo)

    return resultados
