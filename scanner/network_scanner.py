import socket 

def escanear_puertos(ip, puertos):
    resultados = []

    for puerto in puertos:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        resultado = sock.connect_ex((ip, puerto))

        if resultado == 0:
            estado = 'abierto'
            resultados.append((puerto, estado))
        else:
            estado = 'cerrado'
            resultados.append((puerto, estado))
        
        sock.close()

    return resultados

