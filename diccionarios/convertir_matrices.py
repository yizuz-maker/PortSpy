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
