from scanner.network_scanner import escanear_puertos
from matrices.operaciones_matriz import crear_matriz
from cadenas.strings_utils import limpiar_ip
from archivos.leer_ips import leer_ips_desde_txt
import json

def procesar_host_unico(ip, puertos, threads):
    ip = limpiar_ip(ip)
    resultados = escanear_puertos(ip, puertos, threads)
    matriz = crear_matriz(ip, resultados)
    return matriz


def procesar_multiples_hosts(archivo, puertos, threads):
    hosts = leer_ips_desde_txt(archivo)

    matriz_general = []

    for host in hosts:
        matriz_host_unico = procesar_host_unico(host, puertos, threads)
        matriz_general.extend(matriz_host_unico)

    return matriz_general

