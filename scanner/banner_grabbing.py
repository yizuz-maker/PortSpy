"""
Obtiene el banner del servicio desde un socket abierto.

@param sock El socket conectado a un puerto abierto.
@return Los primeros bytes recibidos del servicio (hasta 1024 bytes).
"""
def obtener_banner(sock):
    return sock.recv(1024)

"""
Decodifica el banner recibido en formato raw (bytes) a una cadena legible.

@param banner_raw El banner recibido como bytes.
@return El banner decodificado como string, sin espacios al inicio o al final.
"""
def decodificar_banner(banner_raw):
    return banner_raw.decode().strip()

"""
Envía una solicitud HTTP GET para obtener el banner del servicio web en el puerto 80.

@param ip La dirección IP del host al que se envía la solicitud.
@param sock El socket previamente conectado al puerto 80.
@return El mismo socket después de enviar la solicitud HTTP.
"""
def obtener_banner_http(ip, sock):
    solicitud = "GET / HTTP/1.1\r\nHost: {}\r\n\r\n".format(ip)
    sock.sendall(solicitud.encode())

    return sock

"""
Extrae el nombre del servidor web desde el banner HTTP recibido.

@param banner_dirty El banner HTTP completo como cadena de texto.
@return El valor del encabezado 'Server' si está presente, o una cadena vacía si no se encuentra.
"""
def determinar_http_service(banner_dirty):
    headers = banner_dirty.split("\n")
    banner = ""
    for line in headers:
        if line.startswith("Server"):
            banner = line.replace("Server: ", "").strip()
    return banner
