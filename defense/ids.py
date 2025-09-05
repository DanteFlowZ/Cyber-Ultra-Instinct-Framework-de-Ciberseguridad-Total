#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ids.py - Mini Sistema de Detección de Intrusos
----------------------------------------------
Este script analiza el archivo de logs del honeypot en tiempo real
y detecta comportamientos sospechosos, como múltiples intentos de acceso
desde la misma IP en un corto periodo de tiempo.

Características:
- Lectura en tiempo real de honeypot.log
- Detección de intentos repetidos desde la misma IP
- Umbral configurable de intentos fallidos
- Generación de alertas en consola y en alerts.log

⚠️ Aviso legal:
Este script es únicamente para fines educativos en entornos
controlados. El uso contra sistemas de terceros sin autorización
es ilegal y contrario a la ética profesional.
"""

import time
import logging
from collections import defaultdict
from datetime import datetime, timedelta
import argparse
from colorama import Fore, Style, init

# Inicializar colorama
init(autoreset=True)

# Configuración de logging de alertas
logging.basicConfig(
    filename="alerts.log",
    level=logging.INFO,
    format="%(asctime)s - %(message)s",
)

# ----------------------------
# IDS Core
# ----------------------------
def start_ids(logfile: str, threshold: int, window: int):
    print(f"{Fore.GREEN}[+] IDS iniciado. Monitoreando {logfile}")
    print(f"{Fore.YELLOW}[!] Umbral: {threshold} intentos en {window} segundos\n")

    attempts = defaultdict(list)  # {ip: [timestamps]}

    with open(logfile, "r") as f:
        # Ir al final del archivo
        f.seek(0, 2)

        while True:
            line = f.readline()
            if not line:
                time.sleep(1)
                continue

            # Buscar patrones de conexión
            if "Conexión desde" in line or "dijo:" in line:
                ip = extract_ip(line)
                timestamp = datetime.now()
                attempts[ip].append(timestamp)

                # Limpiar intentos antiguos
                attempts[ip] = [
                    t for t in attempts[ip] if t > timestamp - timedelta(seconds=window)
                ]

                if len(attempts[ip]) >= threshold:
                    alert_msg = f"[ALERTA] Posible ataque de fuerza bruta desde {ip}"
                    print(f"{Fore.RED}{alert_msg}")
                    logging.info(alert_msg)
                    attempts[ip] = []  # reiniciar contador tras alerta


# ----------------------------
# Extraer IP de línea de log
# ----------------------------
def extract_ip(line: str) -> str:
    parts = line.split()
    for part in parts:
        if part.count(".") == 3:  # formato básico IPv4
            return part.split(":")[0]
    return "UNKNOWN"


# ----------------------------
# Argumentos
# ----------------------------
def parse_arguments():
    parser = argparse.ArgumentParser(
        description="Mini IDS para analizar logs del honeypot"
    )
    parser.add_argument(
        "-l", "--logfile", default="honeypot.log", help="Archivo de log a monitorizar"
    )
    parser.add_argument(
        "-t", "--threshold", type=int, default=5, help="Intentos máximos antes de alerta"
    )
    parser.add_argument(
        "-w", "--window", type=int, default=60, help="Ventana de tiempo en segundos"
    )
    return parser.parse_args()


# ----------------------------
# Main
# ----------------------------
if __name__ == "__main__":
    args = parse_arguments()
    try:
        start_ids(args.logfile, args.threshold, args.window)
    except KeyboardInterrupt:
        print(f"\n{Fore.RED}[!] IDS detenido por el usuario.")
