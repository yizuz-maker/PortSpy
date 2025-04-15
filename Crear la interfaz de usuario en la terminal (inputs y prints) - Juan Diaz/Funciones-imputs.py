import socket
import ipaddress
import threading
import queue
import re
def obtener_configuracion():

    red = input("🔌 Ingresá la red a escanear (por ejemplo, 192.168.1.0/24): ").strip()

    modo = input("🎯 ¿Querés escanear un solo puerto, un rango o varios? (1/r/v): ").strip().lower()
    if modo == 'v':
        puertos_input = input("📍 Ingresá los puertos separados por coma (por ejemplo: 22,80,443): ").strip()
        puertos = [int(p) for p in re.findall(r'\d+', puertos_input)]
    elif modo == 'r':
        puertos_input= input("📍 Ingresá el rango de puertos (por ejemplo: 1-65535): ")
        inicio, fin = puertos_input.split('-')
        puertos = list(range(int(inicio), int(fin) + 1))
    else:
        puerto_input = input("📍 Ingresá el puerto a escanear (por defecto 80): ").strip()
        puerto = int(puerto_input) if puerto_input.isdigit() else 80
        puertos = [puerto]P

    hilos_input = input("⚙️  Ingresá la cantidad de hilos (por defecto 100): ").strip()
    hilos = int(hilos_input) if hilos_input.isdigit() else 100

    # timeout_input = input("⏱️  Ingresá el tiempo de espera en segundos (por defecto 1): ").strip()
    # try:
    #     timeout = float(timeout_input)
    # except ValueError:
    #     timeout = 1

    return red, puertos, hilos

M;]ñ
;-{
        .{41{N JKLV,G HJNK,-BVBGHJ{444































Aprint(obtener_configuracion())
