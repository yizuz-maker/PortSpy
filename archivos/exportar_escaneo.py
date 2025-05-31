import json
import os

def exportar_json(resultados, nombre_archivo):
    base = os.path.splitext(nombre_archivo)[0]
    nombre_archivo_final = base + ".json"

    with open(nombre_archivo_final, "w", encoding="utf-8") as f:
        json.dump(resultados, f, indent=4, ensure_ascii=False)

