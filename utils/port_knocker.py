#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
port_knocker.py - Cliente de Port Knocking
------------------------------------------
Este script envía una secuencia de "golpes" (paquetes) a distintos
puertos en un servidor, con el objetivo de activar un servicio oculto.

Características:
- Soporta secuencias TCP o UDP
- Configurable desde línea de comandos
- Secuencias de puertos personalizadas
- Útil para pruebas de seguridad y aprendizaje

⚠️ Aviso legal:
Este script es únicamente para fines educativos en entornos
controlados. El uso contra sistemas de terceros sin autorización
es ilegal y contrario a la ética profesional.
"""

import socket
import argparse
import time
from colorama import Fore, Style, init

# Inicializar colorama
init(autoreset=True)

# ----------------------------
# Enviar golpe
# ----------------------------
def knock(host: str, port: int, protocol: str, delay: float):
    try:
        if protocol == "tcp":
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(1)
            s.connect_ex((host, port))  # No importa si está cerrado
            s.close()
        elif protocol == "udp":
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.sendto(b"knock", (host, port))
            s.close()

        print(f"{Fore.CYAN}[+] Knock en {protocol.upper()} {host}:{port}")
        time.sleep(delay)
    except Exception as e:
        print(f"{Fore.RED}[X] Error en {host}:{port} -> {e}")


# ----------------------------
# Cliente de Port Knocking
# ----------------------------
def start_knock(host: str, ports: list, protocol: str, delay: float):
    print(f"{Fore.GREEN}[+] Iniciando port knocking hacia {host}")
    print(f"{Fore.YELLOW}[!] Secuencia: {ports} | Protocolo: {protocol.upper()}\n")

    for port in ports:
        knock(host, port, protocol, delay)

    print(f"{Fore.MAGENTA}[✓] Secuencia completada. Intenta conectar al servicio oculto.")


# ----------------------------
# Argumentos
# ----------------------------
def parse_arguments():
    parser = argparse.ArgumentParser(description="Cliente de Port Knocking")
    parser.add_argument("-H", "--host", required=True, help="Host objetivo")
    parser.add_argument(
        "-P", "--ports", required=True,
        help="Secuencia de puertos separados por comas (ej: 7000,8000,9000)"
    )
    parser.add_argument(
        "-p", "--protocol", choices=["tcp", "udp"], default="tcp", help="Protocolo (tcp/udp)"
    )
    parser.add_argument(
        "-d", "--delay", type=float, default=0.5, help="Retraso entre golpes (segundos)"
    )
    return parser.parse_args()


# ----------------------------
# Main
# ----------------------------
if __name__ == "__main__":
    args = parse_arguments()
    ports = [int(p.strip()) for p in args.ports.split(",")]
    try:
        start_knock(args.host, ports, args.protocol, args.delay)
    except KeyboardInterrupt:
        print(f"\n{Fore.RED}[!] Port knocking detenido por el usuario.")
