import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from diccionarios.convertir_matrices import matrices_a_diccionario
import pytest 

def test_matrices_a_diccionario():
    matrices = [
        [
            ["192.168.1.1", 22, "abierto", "SSH"],
            ["192.168.1.1", 80, "abierto", "Apache"]
        ],
        [
            ["192.168.1.2", 443, "cerrado", ""],
            ["192.168.1.2", 21, "abierto", "FTP"]
        ]
    ]

    esperado = {
        "192.168.1.1": [
            {"puerto": 22, "estado": "abierto", "banner": "SSH"},
            {"puerto": 80, "estado": "abierto", "banner": "Apache"}
        ],
        "192.168.1.2": [
            {"puerto": 443, "estado": "cerrado", "banner": ""},
            {"puerto": 21, "estado": "abierto", "banner": "FTP"}
        ]
    }

    resultado = matrices_a_diccionario(matrices)
    assert resultado == esperado
