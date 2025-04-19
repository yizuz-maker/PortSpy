from functools import reduce

#Matriz: [[IP, Puerto, Estado], ...]

"""
Obtiene una lista de puertos abiertos a partir de una matriz de datos.

@param matriz Una lista de listas donde cada sublista representa un puerto y su estado.
@return Una lista con los números de puertos que están abiertos.
"""
def obtener_puertos_abiertos(matriz):
    abiertos = list(filter(lambda fila: fila[2] == 'abierto', matriz)) #Devuelve una lista de puertos abiertos usando filter y lambda 
    return [fila[1] for fila in abiertos]

"""
Cuenta la cantidad de puertos abiertos en una matriz de datos.

@param matriz Una lista de listas donde cada sublista representa un puerto y su estado.
@return La cantidad de puertos que están abiertos.
"""
def contar_puertos_abiertos(matriz):
    return reduce(lambda acc, fila: acc + (1 if fila[2] == 'abierto' else 0), matriz, 0)     #Cuenta la cantidad de puertos abiertos usando reduce

"""
Ordena la matriz de datos por número de puerto.

@param matriz Una lista de listas donde cada sublista representa un puerto y su estado.
@param reversa Indica si se debe ordenar en orden descendente (por defecto es False).
@return La matriz ordenada por número de puerto.
"""
def ordenar_por_puerto(matriz, reversa=False):
    return sorted(matriz, key=lambda fila: fila[1], reverse=reversa) #Devuelve la matriz ordenada por número de puerto

"""
Extrae una sublista de filas desde la matriz de puertos, usando índices de inicio y fin.

@param matriz Una lista de listas donde cada sublista representa un puerto y su estado.
@param inicio El índice de inicio (inclusive).
@param fin El índice de fin (exclusivo).
@return Una sublista de la matriz con las filas dentro del rango especificado.
"""
def extraer_sublista_puertos(matriz, inicio, fin):
    return matriz[inicio:fin] #Devuelve una sublista de filas entre los índices dados (slicing)
