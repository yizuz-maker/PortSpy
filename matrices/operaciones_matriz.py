def crear_matriz(ip, resultados):
    """
    Crea una matriz con los resultados de escaneo para una IP específica.
    Matriz: [[IP, Puerto, Estado], ...]
    """
    matriz = []
    for puerto, estado in resultados:
        matriz.append([ip, puerto, estado])
    return matriz

def mostrar_matriz(matriz):
    print("\n=== MATRIZ DE RESULTADOS ===")
    print(f"{'IP':<15} {'Puerto':<10} {'Estado':<10}")
    print("-" * 35)
    for fila in matriz:
        print(f"{fila[0]:<15} {fila[1]:<10} {fila[2]:<10}")
