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
