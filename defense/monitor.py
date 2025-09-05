#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
monitor.py - Monitor de logs en tiempo real
-------------------------------------------
Este script permite visualizar en vivo la actividad de los logs
del honeypot o del IDS con colores y categorización de eventos.

Características:
- Lectura continua tipo `tail -f`
- Soporte para múltiples archivos de log (honeypot.log, alerts.log, etc.)
- Colores según el tipo de evento
- Salida clara para análisis en tiempo real

⚠️ Aviso legal:
Este script es únicamente para fines educativos en entornos
controlados. El uso contra sistemas de terceros sin autorización
es ilegal y contrario a la ética profesional.
"""

import time
import argparse
from colorama import Fore, Style, init

# Inicializar colorama
init(autoreset=True)


# ----------------------------
# Función principal
# ----------------------------
def monitor_log(logfile: str):
    print(f"{Fore.GREEN}[+] Monitorizando {logfile} en tiempo real...\n")

    with open(logfile, "r") as f:
        # Ir al final del archivo
        f.seek(0, 2)

        while True:
            line = f.readline()
            if not line:
                time.sleep(0.5)
                continue

            # Clasificar tipo de evento
            if "Conexión desde" in line:
                print(f"{Fore.CYAN}[CONEXIÓN] {line.strip()}")
            elif "dijo:" in line:
                print(f"{Fore.MAGENTA}[INTENTO] {line.strip()}")
            elif "[ALERTA]" in line:
                print(f"{Fore.RED}{Style.BRIGHT}{line.strip()}")
            elif "Error" in line or "WARNING" in line:
                print(f"{Fore.YELLOW}[ERROR] {line.strip()}")
            else:
                print(f"{Fore.WHITE}{line.strip()}")


# ----------------------------
# Argumentos
# ----------------------------
def parse_arguments():
    parser = argparse.ArgumentParser(
        description="Monitor en tiempo real de logs (honeypot o IDS)"
    )
    parser.add_argument(
        "-l", "--logfile", default="honeypot.log", help="Archivo de log a monitorizar"
    )
    return parser.parse_args()


# ----------------------------
# Main
# ----------------------------
if __name__ == "__main__":
    args = parse_arguments()
    try:
        monitor_log(args.logfile)
    except KeyboardInterrupt:
        print(f"\n{Fore.RED}[!] Monitor detenido por el usuario.")
