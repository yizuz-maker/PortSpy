from scanner.network_scanner import escanear_puertos
from matrices.operaciones_matriz import crear_matriz
from cadenas.strings_utils import limpiar_ip, validar_ip
from archivos.leer_ips import leer_ips_desde_txt
from archivos.leer_ips import leer_ips_desde_json
import json

"""
Procesa una única dirección IP: la limpia, valida, escanea los puertos y genera la matriz de resultados.

@param ip La dirección IP a procesar.
@param puertos Lista de puertos a escanear.
@param threads Número de hilos a utilizar en el escaneo.
@return Una matriz con el formato [[IP, Puerto, Estado, Banner], ...].

@raise ValueError Si la IP proporcionada no es válida.
"""
def procesar_host_unico(ip, puertos, threads):
    ip = limpiar_ip(ip)
    if not validar_ip(ip):
        raise ValueError(f"La IP proporcionada no es valida: {ip}")
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

"""
Procesa múltiples hosts y sus respectivos puertos a partir de un archivo JSON.

@param archivo Ruta al archivo JSON con formato { "IP": [puertos], ... }.
@param threads Número de hilos a utilizar para el escaneo.
@return Una matriz general con los resultados del escaneo de todos los hosts.
"""
def procesar_multiples_hosts_puertos(archivo, threads):
    data = leer_ips_desde_json(archivo)
    matriz_general = []

    for ip in data:
        puertos = data[ip]
        matriz_ip = procesar_host_unico(ip, puertos, threads)
        matriz_general.extend(matriz_ip)

    return matriz_general

