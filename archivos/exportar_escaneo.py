import json
import os

"""
Exporta una lista de resultados a un archivo JSON.

@param resultados Los resultados de escaneo.
@param nombre_archivo El nombre base del archivo; se le añade la extensión .json automáticamente.
"""
def exportar_json(resultados, nombre_archivo):
    base = os.path.splitext(nombre_archivo)[0]
    nombre_archivo_final = base + ".json"

    with open(nombre_archivo_final, "w", encoding="utf-8") as f:
        json.dump(resultados, f, indent=4, ensure_ascii=False)

"""
Exporta una cadena de texto a un archivo .txt.

@param resultados String que contiene el texto a escribir en el archivo.
@param nombre_archivo Nombre base del archivo. Si no termina en ".txt", se reemplaza o agrega la extensión automáticamente.

@nota Si `nombre_archivo` incluye una ruta, el archivo se guarda en esa ubicación.
"""
def exportar_txt(resultados, nombre_archivo):
    base = os.path.splitext(nombre_archivo)[0]
    nombre_archivo_final = base + ".txt"

    with open(nombre_archivo_final, "w", encoding="utf-8") as f:
        f.write(resultados)
