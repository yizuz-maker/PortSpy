"""
Devuelve un diccionario donde la IP es la clave y los valores
son una lista de resultados por puerto:

  {
      "192.168.1.10": [{"puerto": 22, "estado": "abierto", "banner":"apache 2.3.4"}, ...]
  }
"""

def construir_escaneos_por_ip(ip, resultados):

    escaneos = {}

    escaneos[ip] = []

    for puerto, estado, banner in resultados:
        escaneos[ip].append({
            "puerto": puerto,
            "estado": estado,
            "banner": banner
        })

    return escaneos