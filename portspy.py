import socket
import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed
from colorama import Fore, init

init(autoreset=True)

common_ports = {
    20: "FTP-DATA", 21: "FTP", 22: "SSH", 23: "TELNET", 25: "SMTP",
    53: "DNS", 80: "HTTP", 110: "POP3", 143: "IMAP", 443: "HTTPS",
    3306: "MySQL", 3389: "RDP"
}

def scan_port(ip, port, timeout=1):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)
        result = sock.connect_ex((ip, port))
        sock.close()
        if result == 0:
            service = common_ports.get(port, "Desconocido")
            print(f"{Fore.GREEN}[+] Puerto {port} abierto ({service})")
            return port, service
    except Exception as e:
        print(f"{Fore.RED}[!] Error al escanear puerto {port}: {e}")
    return None

def get_arguments():
    parser = argparse.ArgumentParser(description="PortSpy")
    parser.add_argument("ip", help="Dirección IP")
    parser.add_argument("-p", "--ports", help="Rango de puertos (por defecto: 1-1024)", default="1-1024")
    parser.add_argument("-t", "--threads", help="Número de hilos (por defecto: 100)", type=int, default=100)
    parser.add_argument("--common", help="Escanear solo los puertos comunes", action="store_true")
    return parser.parse_args()

def main():
    args = get_arguments()
    ip = args.ip
    max_threads = args.threads

    if args.common:
        ports_to_scan = list(common_ports.keys())
        print(f"{Fore.CYAN}Escaneando {ip} en puertos comunes: {ports_to_scan}\n")
    else:
        start_port, end_port = map(int, args.ports.split("-"))
        ports_to_scan = list(range(start_port, end_port + 1))
        print(f"{Fore.CYAN}Escaneando {ip} en el rango de puertos {start_port}-{end_port}...\n")

    open_ports = []

    with ThreadPoolExecutor(max_workers=max_threads) as executor:
        future_to_port = {
            executor.submit(scan_port, ip, port): port for port in ports_to_scan
        }

        for future in as_completed(future_to_port):
            result = future.result()
            if result:
                open_ports.append(result)

    print(f"\n{Fore.YELLOW}Resumen de puertos abiertos en {ip}:")
    if open_ports:
        for port, service in open_ports:
            print(f"  - Puerto {port} ({service})")
    else:
        print(f"{Fore.RED}No se encontraron puertos abiertos.")

if __name__ == "__main__":
    main()
