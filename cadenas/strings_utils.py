def limpiar_ip(ip):
    return ip.strip() # Elimina espacios en blanco

def normalizar_estado(estado):
    return estado.lower() # Pasa todo a minusculas

def comparar_estado(estado, valor):
    return estado.strip().lower() == valor.strip().lower()

def obtener_prefix(ip): # Devuelve el prefijo (primeros 3 octetos)
    partes = ip.strip().split('.') # Separa los octetos 
    if len(partes) == 4:
        prefijo = '.'.join(partes[:3])
        return prefijo
    else:
        return ip # tendria que elevarse un error



