#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
honeypot.py - Honeypot TCP básico
---------------------------------
Este script simula un servicio vulnerable para atraer atacantes
y registrar sus interacciones.

Características:
- Escucha en un puerto TCP configurable (ej: 2222 simulando SSH).
- Registra cada conexión en un archivo de log.
- Envía banners falsos para parecer real.
- Responde de forma engañosa a los comandos enviados.

⚠️ Aviso legal:
Este script es únicamente para fines educativos en entornos
controlados. El uso contra sistemas de terceros sin autorización
es ilegal y contrario a la ética profesional.
"""

import socket
import logging
from datetime import datetime
import argparse
from colorama import Fore, Style, init

# Inicializar colorama
init(autoreset=True)

# Configuración de logging
logging.basicConfig(
    filename="honeypot.log",
    level=logging.INFO,
    format="%(asctime)s - %(message)s",
)

# ----------------------------
# Honeypot Server
# ----------------------------
def start_honeypot(host: str, port: int):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen(5)

    print(f"{Fore.GREEN}[+] Honeypot escuchando en {host}:{port}...")
    print(f"{Fore.YELLOW}[!] Todos los intentos serán registrados en honeypot.log\n")

    while True:
        conn, addr = server.accept()
        ip, remote_port = addr
        print(f"{Fore.CYAN}[+] Conexión desde {ip}:{remote_port}")

        # Registrar en log
        logging.info(f"Conexión desde {ip}:{remote_port}")

        # Enviar banner falso (ej: SSH)
        conn.send(b"SSH-2.0-OpenSSH_7.9p1 Ubuntu-10\n")
        logging.info(f"Enviado banner falso a {ip}")

        while True:
            try:
                data = conn.recv(1024).decode(errors="ignore").strip()
                if not data:
                    break

                print(f"{Fore.MAGENTA}[DATA] {ip}:{remote_port} -> {data}")
                logging.info(f"{ip}:{remote_port} dijo: {data}")

                # Respuesta engañosa
                response = "Acceso denegado. Credenciales incorrectas.\n"
                conn.send(response.encode())
            except Exception as e:
                logging.warning(f"Error con {ip}: {e}")
                break

        conn.close()
        print(f"{Fore.RED}[!] Conexión cerrada con {ip}:{remote_port}")


# ----------------------------
# Argumentos
# ----------------------------
def parse_arguments():
    parser = argparse.ArgumentParser(
        description="Honeypot TCP básico (uso educativo)"
    )
    parser.add_argument(
        "-H", "--host", default="0.0.0.0", help="Host para escuchar (por defecto: 0.0.0.0)"
    )
    parser.add_argument(
        "-p", "--port", type=int, default=2222, help="Puerto para el honeypot (por defecto: 2222)"
    )
    return parser.parse_args()


# ----------------------------
# Main
# ----------------------------
if __name__ == "__main__":
    args = parse_arguments()
    try:
        start_honeypot(args.host, args.port)
    except KeyboardInterrupt:
        print(f"\n{Fore.RED}[!] Honeypot detenido por el usuario.")
