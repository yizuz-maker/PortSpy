import re
"""
Elimina los espacios en blanco al principio y al final de una dirección IP.

@param ip La dirección IP a limpiar.
@return La dirección IP sin espacios en blanco.
"""
def limpiar_ip(ip):
    return ip.strip()

"""
Valida si una dirección IP es una IPv4 válida.

@param ip La dirección IP a validar.
@return True si la IP es válida; False en caso contrario.
"""
def validar_ip(ip):
    ip_regex = (
        r"^(?:(?:25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)\.){3}"
        r"(?:25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)$"
    )
    return re.match(ip_regex, ip.strip()) is not None

"""
Convierte el estado a minúsculas para su normalización.

@param estado El estado a normalizar.
@return El estado en minúsculas.
"""
def normalizar_estado(estado):
    return estado.lower() # Pasa todo a minusculas

"""
Compara dos estados ignorando mayúsculas y espacios en blanco.

@param estado El primer estado a comparar.
@param valor El segundo estado a comparar.
@return True si ambos estados son iguales tras normalizarlos; False en caso contrario.
"""
def comparar_estado(estado, valor):
    return estado.strip().lower() == valor.strip().lower()

"""
Devuelve el prefijo de una dirección IP, compuesto por los primeros tres octetos.

@param ip La dirección IP de la cual obtener el prefijo.
@return El prefijo de la IP si es válida; en caso contrario, devuelve la IP original.
"""
def obtener_prefix(ip): # Devuelve el prefijo (primeros 3 octetos)
    partes = ip.strip().split('.') # Separa los octetos 
    if len(partes) == 4:
        prefijo = '.'.join(partes[:3])
        return prefijo
    else:
        return ip # tendria que elevarse un error



