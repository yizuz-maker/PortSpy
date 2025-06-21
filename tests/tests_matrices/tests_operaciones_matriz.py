import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from matrices.operaciones_matriz import crear_matriz, mostrar_matriz
import pytest 

# ip = 192.168.1.20
# resultado = puerto, estado, banner_decoded

def test_crear_matriz():
    ip = "192.168.1.20"
    puerto = 22
    estado = "abierto"
    banner = "SSH-2.0-OpenSSH_7.9p1 Debian-10+deb10u2"

    matriz_resultado = []
    matriz_resultado = crear_matriz(ip, [(puerto, estado, banner)])

    matriz_esperada = []
    matriz_esperada = [[[ip, puerto, estado, banner]]]

    assert matriz_resultado == matriz_esperada 


def test_mostrar_matriz(capsys):
    matriz = [
        ["192.168.1.20", 22, "abierto", "SSH-2.0-OpenSSH_7.9p1 Debian-10+deb10u2"]
    ]

    mostrar_matriz(matriz)

    capturado = capsys.readouterr()
    salida = capturado.out

    assert "192.168.1.20" in salida
    assert "22" in salida
    assert "abierto" in salida
    assert "SSH-2.0-OpenSSH_7.9p1 Debian-10+deb10u2" in salida
    assert "=== MATRIZ DE RESULTADOS ===" in salida
