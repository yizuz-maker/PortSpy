import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from matrices.operaciones_matriz import crear_matriz
import pytest 

# ip = 192.168.1.20
# resultado = puerto, estado, banner_decoded

def test_answer():
    ip = "192.168.1.20"
    puerto = 22
    estado = "abierto"
    banner = "SSH-2.0-OpenSSH_7.9p1 Debian-10+deb10u2"

    matriz_resultado = []
    matriz_resultado = crear_matriz(ip, [(puerto, estado, banner)])

    matriz_esperada = []
    matriz_esperada = [[ip, puerto, estado, banner]]

    assert matriz_resultado == matriz_esperada 
