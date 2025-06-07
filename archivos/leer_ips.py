import json

"""
    Lee un archivo de texto con una IP por linea
    Ignora lineas vacias
"""
def leer_ips_desde_txt(path):
    ips = []
    try:
        with open(path, 'r') as f:
            for linea in f:
                linea = linea.strip()
                if linea and not linea.startswith("#"):
                    ips.append(linea)
    except FileNotFoundError:
        print(f"Error archivo no encontrado: {path}")
    except Exception as e:
        print(f"Error al leer el archivo: {e}")

    return ips

"""
Lee un archivo JSON que contiene direcciones IP como claves y listas de puertos como valores.

@param path Ruta al archivo JSON a leer.
@return Un diccionario con formato { "IP": [puerto1, puerto2, ...] }. 
         Si ocurre un error, devuelve un diccionario vacío.
"""
def leer_ips_desde_json(path):
    try:
        with open(path, 'r') as f:
            data = json.load(f)

        if not isinstance(data, dict):
            raise ValueError("El archivo JSON debe contener un diccionario con IPs como claves y listas de puertos como valores.")

        for ip, puertos in data.items():
            if not isinstance(puertos, list) or not all(isinstance(p, int) for p in puertos):
                raise ValueError(f"Formato inválido para los puertos de {ip}. Debe ser una lista de enteros.")

        return data

    except FileNotFoundError:
        print(f"Archivo no encontrado: {path}")
    except json.JSONDecodeError as e:
        print(f"Error al parsear JSON: {e}")
    except Exception as e:
        print(f"Error desconocido: {e}")

    return {}


