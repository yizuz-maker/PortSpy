import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from diccionarios.estructura_datos import construir_escaneos_por_ip
import pytest 

from cadenas.strings_utils import (
    limpiar_ip,
    validar_ip,
    normalizar_estado,
    comparar_estado,
    obtener_prefix
)

def test_limpiar_ip():
    assert limpiar_ip(" 192.168.1.1 ") == "192.168.1.1"
    assert limpiar_ip("\t10.0.0.1\n") == "10.0.0.1"

def test_validar_ip():
    assert validar_ip("192.168.1.1") is True
    assert validar_ip("255.255.255.255") is True
    assert validar_ip("0.0.0.0") is True
    assert validar_ip("999.999.999.999") is False
    assert validar_ip("192.168.1") is False
    assert validar_ip("abc.def.ghi.jkl") is False
    assert validar_ip(" 192.168.1.1 ") is True  

def test_normalizar_estado():
    assert normalizar_estado("ABIERTO") == "abierto"
    assert normalizar_estado(" Cerrado ") == " cerrado ".lower()

def test_comparar_estado():
    assert comparar_estado("ABIERTO", "abierto") is True
    assert comparar_estado(" cerrado ", "CERRADO") is True
    assert comparar_estado("abierto", "cerrado") is False

def test_obtener_prefix():
    assert obtener_prefix("192.168.1.100") == "192.168.1"
    assert obtener_prefix("10.0.0.1") == "10.0.0"
    assert obtener_prefix("192.168.1") == "192.168.1"  
