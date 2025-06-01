from scanner.network_scanner import escanear_puertos
from matrices.operaciones_matriz import crear_matriz
from cadenas.strings_utils import limpiar_ip
from archivos.leer_ips import leer_ips_desde_txt
import json

"""
Procesa una única dirección IP: limpia la IP, escanea los puertos y genera la matriz de resultados.

@param ip La dirección IP a procesar.
@param puertos Lista de puertos a escanear.
@param threads Número de hilos (si se utiliza en el escaneo paralelo, sino 10 por default).
@return Una matriz con el formato [[IP, Puerto, Estado, Banner], ...] si se incluye información de banner.
"""
def procesar_host_unico(ip, puertos, threads):
    ip = limpiar_ip(ip)
    resultados = escanear_puertos(ip, puertos, threads)
    matriz = crear_matriz(ip, resultados)
    return matriz

"""
Procesa múltiples direcciones IP desde un archivo de texto: escanea los puertos de cada host y construye una matriz general de resultados.

@param archivo Ruta del archivo .txt que contiene una IP por línea.
@param puertos Lista de puertos a escanear para cada IP.
@param threads Número de hilos (si se utiliza en el escaneo paralelo).
@return Una matriz combinada con los resultados de todos los hosts escaneados.
"""
def procesar_multiples_hosts(archivo, puertos, threads):
    hosts = leer_ips_desde_txt(archivo)

    matriz_general = []

    for host in hosts:
        matriz_host_unico = procesar_host_unico(host, puertos, threads)
        matriz_general.extend(matriz_host_unico)

    return matriz_general

