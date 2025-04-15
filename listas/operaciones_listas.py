from functools import reduce

def obtener_puertos_abiertos(matriz):
    abiertos = list(filter(lambda fila: fila[2] == 'abierto', matriz)) #Devuelve una lista de puertos abiertos usando filter y lambda 
    return [fila[1] for fila in abiertos]

def contar_puertos_abiertos(matriz):
    return reduce(lambda acc, fila: acc + (1 if fila[2] == 'abierto' else 0), matriz, 0)     #Cuenta la cantidad de puertos abiertos usando reduce

def ordenar_por_puerto(matriz, reversa=False):
    return sorted(matriz, key=lambda fila: fila[1], reverse=reversa) #Devuelve la matriz ordenada por número de puerto

def extraer_sublista_puertos(matriz, inicio, fin):
    return matriz[inicio:fin] #Devuelve una sublista de filas entre los índices dados (slicing)
