"""
Crea una matriz con los resultados de escaneo para una IP específica.

@param ip La dirección IP a la que pertenecen los resultados.
@param resultados Una lista de tuplas con pares (puerto, estado).
@return Una matriz con el formato [[IP, Puerto, Estado], ...].
"""

def crear_matriz(ip, resultados):
    """
    Matriz con los resultados de escaneo para una IP específica.
    Matriz: [[IP, Puerto, Estado, Banner], ...]
    """
    matriz = []
    for puerto, estado, banner in resultados:
        matriz.append([ip, puerto, estado, banner])
    return matriz

"""
Muestra en consola una matriz de resultados de escaneo de puertos.

@param matriz Una lista de listas con la información de los puertos y su estado.
Cada sublista tiene el formato [IP, Puerto, Estado].
"""
def mostrar_matriz(matriz):
    print("\n=== MATRIZ DE RESULTADOS ===")
    print(f"{'IP':<15} {'Puerto':<10} {'Estado':<10} {'Banner':<10}")
    print("-" * 45)
    for fila in matriz:
        print(f"{fila[0]:<15} {fila[1]:<10} {fila[2]:<10} {fila[3]:<10}")
