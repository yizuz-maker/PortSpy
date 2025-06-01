"""
Convierte una lista de matrices de resultados en un diccionario organizado por IP.

@param matrices Lista de matrices, donde cada matriz contiene filas con información de escaneo [IP, puerto, estado, banner].
@return Un diccionario con las IPs como claves y una lista de diccionarios con los detalles de cada puerto como valores.
"""
def matrices_a_diccionario(matrices):
    resultado = {}

    for matriz in matrices:
        for fila in matriz:
            ip, puerto, estado, banner = fila
            if ip not in resultado:
                resultado[ip] = []
            resultado[ip].append({
                "puerto": puerto,
                "estado": estado,
                "banner": banner
            })

    return resultado
