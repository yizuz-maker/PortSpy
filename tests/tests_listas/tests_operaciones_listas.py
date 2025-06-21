import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from listas.operaciones_listas import obtener_puertos_abiertos, contar_puertos_abiertos, ordenar_por_puerto, extraer_sublista_puertos
import pytest 


import pytest
from listas.operaciones_listas import (
    obtener_puertos_abiertos,
    contar_puertos_abiertos,
    ordenar_por_puerto,
    extraer_sublista_puertos
)

matriz_ejemplo = [
    ["192.168.1.20", 21, "cerrado", ""],
    ["192.168.1.20", 22, "abierto", "SSH"],
    ["192.168.1.20", 80, "abierto", "Apache"],
    ["192.168.1.20", 443, "cerrado", ""],
    ["192.168.1.20", 8080, "abierto", "HTTP"]
]

def test_obtener_puertos_abiertos():
    abiertos = obtener_puertos_abiertos(matriz_ejemplo)
    assert abiertos == [22, 80, 8080]

def test_contar_puertos_abiertos():
    cantidad = contar_puertos_abiertos(matriz_ejemplo)
    assert cantidad == 3

def test_ordenar_por_puerto_ascendente():
    ordenada = ordenar_por_puerto(matriz_ejemplo)
    puertos = [fila[1] for fila in ordenada]
    assert puertos == [21, 22, 80, 443, 8080]

def test_ordenar_por_puerto_descendente():
    ordenada = ordenar_por_puerto(matriz_ejemplo, reversa=True)
    puertos = [fila[1] for fila in ordenada]
    assert puertos == [8080, 443, 80, 22, 21]

def test_extraer_sublista_puertos():
    sublista = extraer_sublista_puertos(matriz_ejemplo, 1, 4)
    assert len(sublista) == 3
    assert sublista[0][1] == 22
    assert sublista[-1][1] == 443

