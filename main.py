import argparse
from scanner.network_scanner import escanear_puertos
from matrices.operaciones_matriz import crear_matriz, mostrar_matriz
from listas.operaciones_listas import obtener_puertos_abiertos, contar_puertos_abiertos, ordenar_por_puerto
from cadenas.strings_utils import limpiar_ip, obtener_prefix

def parse_args():
    parser = argparse.ArgumentParser(description="PortSpy - Escaner de puertos en Python")
    parser.add_argument("--ip", required=True, help="Direccion IP a escanear")
    parser.add_argument("--rango", required=True, help="Rango de puertos a escanear (ej: 20-80)")
    return parser.parse_args()

def main():
    args = parse_args()

    ip = limpiar_ip(args.ip)
    inicio, fin = map(int, args.rango.split('-')) # rango pasa a ser ["20", "25"] y luego se mapean para que se pasen a INT
    puertos = list(range(inicio, fin + 1))  # Puertos es una lista tipo [20, 21, 22, 23, 24, 25]

    resultados = escanear_puertos(ip, puertos)

    matriz = crear_matriz(ip, resultados)
    mostrar_matriz(matriz)

    abiertos = obtener_puertos_abiertos(matriz)
    print(f"\nPuertos abiertos detectados: {abiertos}")

    total_abiertos = contar_puertos_abiertos(matriz)
    print(f"Cantidad total de puertos abiertos: {total_abiertos}")

    print("\nMatriz ordenada por número de puerto:")
    matriz_ordenada = ordenar_por_puerto(matriz)
    for fila in matriz_ordenada:
        if fila[2] == 'abierto':
            print(f"{fila[0]:<15} {fila[1]:<10} {fila[2]:<10} {fila[3]:<10}")

    print(f"\nPrefijo de la red: {obtener_prefix(ip)}")

if __name__ == "__main__":
    main()
