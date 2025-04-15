from scanner.network_scanner import escanear_puertos
from matrices.operaciones_matriz import crear_matriz, mostrar_matriz
from listas.operaciones_listas import obtener_puertos_abiertos, contar_puertos_abiertos, ordenar_por_puerto

def main():
    ip = input("Ingrese la IP a escanear: ")
    rango = input("Ingresa el rango de puertos (ej: 20-25): ")

    inicio,fin = map(int, rango.split('-')) # rango pasa a ser ["20", "25"] y luego se mapean para que se pasen a INT
    puertos = list(range(inicio, fin + 1)) # Puertos es una lista tipo [20, 21, 22, 23, 24, 25]

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
            print(f"{fila[0]:<15} {fila[1]:<10} {fila[2]:<10}")

if __name__ == "__main__": # Define que este archivo sea ejecutable
    main()


