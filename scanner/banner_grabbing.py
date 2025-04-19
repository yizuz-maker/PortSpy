def obtener_banner(sock):
    return sock.recv(1024)

def decodificar_banner(banner_raw):
    return banner_raw.decode().strip()


def obtener_banner_http(ip, sock):
    solicitud = "GET / HTTP/1.1\r\nHost: {}\r\n\r\n".format(ip)
    sock.sendall(solicitud.encode())

    return sock

def decodificar_banner_http():
    pass

def determinar_http_service(sock):
    pass 
