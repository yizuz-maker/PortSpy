from scanner.network_scanner import escanear_puertos

def main():
    ip = input("Ingrese la IP a escanear: ")
    rango = input("Ingresa el rango de puertos (ej: 20-25): ")

    inicio,fin = map(int, rango.split('-')) # rango pasa a ser ["20", "25"] y luego se mapean para que se pasen a INT
    puertos = list(range(inicio, fin + 1)) # Puertos es una lista tipo [20, 21, 22, 23, 24, 25]

    resultados = escanear_puertos(ip, puertos) 

    print("\n")
    print("Resumen:")
    for puerto, estado in resultados:
        if estado == 'abierto':
            print(f"Puerto {puerto}: {estado}")

if __name__ == "__main__": # Define que este archivo sea ejecutable
    main()


