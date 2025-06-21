import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from diccionarios.estructura_datos import construir_escaneos_por_ip
import pytest 

def test_construir_escaneos_por_ip():
    ip = "192.168.1.10"
    resultados = [
        (22, "abierto", "SSH"),
        (80, "abierto", "Apache"),
        (443, "cerrado", "")
    ]

    esperado = {
        "192.168.1.10": [
            {"puerto": 22, "estado": "abierto", "banner": "SSH"},
            {"puerto": 80, "estado": "abierto", "banner": "Apache"},
            {"puerto": 443, "estado": "cerrado", "banner": ""}
        ]
    }

    assert construir_escaneos_por_ip(ip, resultados) == esperado
