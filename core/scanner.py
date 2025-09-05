#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
scanner.py - Escáner de puertos TCP (versión avanzada)
------------------------------------------------------
Este script implementa un escaneo de puertos en Python,
con un modo detallado (verbose) que muestra también los puertos cerrados.

Características:
- Escaneo de puertos con rango configurable.
- Muestra puertos abiertos por defecto.
- Modo verbose: también puertos cerrados/filtrados.
- Colores en la salida para mayor claridad.
- Resumen final con estadísticas.

⚠️ Aviso legal:
Este script es únicamente para fines educativos en entornos
controlados. El uso contra sistemas de terceros sin autorización
es ilegal y contrario a la ética profesional.
"""

import socket
import argparse
from datetime import datetime
from colorama import Fore, Style, init

# Inicializar colorama
init(autoreset=True)

# ----------------------------
# Función principal del escáner
# ----------------------------
def scan_ports(target: str, start_port: int, end_port: int, verbose: bool):
    print(f"\n[+] Escaneando host: {target}")
    print(f"[+] Rango de puertos: {start_port}-{end_port}")
    print(f"[+] Inicio: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")

    open_ports = []
    closed_ports = []

    try:
        for port in range(start_port, end_port + 1):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.5)  # Timeout de medio segundo por puerto
            result = sock.connect_ex((target, port))

            if result == 0:
                print(f"{Fore.GREEN}[OPEN] {port}/tcp está abierto ✅")
                open_ports.append(port)
            else:
                if verbose:
                    print(f"{Fore.RED}[CLOSED] {port}/tcp cerrado/filtrado ❌")
                closed_ports.append(port)
            sock.close()

    except KeyboardInterrupt:
        print("\n[!] Escaneo interrumpido por el usuario.")
        return
    except socket.gaierror:
        print("[!] Error: No se pudo resolver el nombre del host.")
        return
    except socket.error:
        print("[!] Error: No se pudo conectar al host.")
        return

    print(f"\n[+] Escaneo finalizado a las {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"[+] Resultados: {len(open_ports)} abiertos / {len(closed_ports)} cerrados")
    if open_ports:
        print(f"[+] Puertos abiertos: {', '.join(map(str, open_ports))}")


# ----------------------------
# Función de argumentos
# ----------------------------
def parse_arguments():
    parser = argparse.ArgumentParser(
        description="Escáner de puertos TCP en Python (uso educativo)"
    )
    parser.add_argument("target", help="Dirección IP o dominio objetivo")
    parser.add_argument(
        "-sp", "--start-port", type=int, default=1, help="Puerto inicial (por defecto: 1)"
    )
    parser.add_argument(
        "-ep", "--end-port", type=int, default=1024, help="Puerto final (por defecto: 1024)"
    )
    parser.add_argument(
        "-v", "--verbose", action="store_true", help="Muestra también puertos cerrados"
    )
    return parser.parse_args()


# ----------------------------
# Main
# ----------------------------
if __name__ == "__main__":
    args = parse_arguments()
    scan_ports(args.target, args.start_port, args.end_port, args.verbose)
