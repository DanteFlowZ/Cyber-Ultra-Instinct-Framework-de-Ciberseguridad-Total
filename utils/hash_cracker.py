#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
hash_cracker.py - Cracker básico de hashes por diccionario
---------------------------------------------------------
Este script intenta romper un hash comparándolo con un diccionario
de contraseñas conocidas.

Características:
- Soporta MD5, SHA1 y SHA256
- Usa un archivo de diccionario proporcionado por el usuario
- Destaca en consola si encuentra la contraseña
- Ejemplo de uso Red Team y Blue Team

⚠️ Aviso legal:
Este script es únicamente para fines educativos en entornos
controlados. El uso contra sistemas de terceros sin autorización
es ilegal y contrario a la ética profesional.
"""

import argparse
import hashlib
from colorama import Fore, Style, init

# Inicializar colorama
init(autoreset=True)

# ----------------------------
# Función para aplicar hash
# ----------------------------
def hash_string(text: str, algorithm: str) -> str:
    h = hashlib.new(algorithm)
    h.update(text.encode("utf-8"))
    return h.hexdigest()


# ----------------------------
# Cracker de hashes
# ----------------------------
def crack_hash(target_hash: str, dictionary: str, algorithm: str):
    print(f"{Fore.GREEN}[+] Iniciando ataque con {algorithm.upper()}...\n")

    with open(dictionary, "r", encoding="utf-8", errors="ignore") as f:
        for line in f:
            candidate = line.strip()
            hashed_candidate = hash_string(candidate, algorithm)

            if hashed_candidate == target_hash:
                print(f"{Fore.CYAN}[ENCONTRADO] Hash: {target_hash}")
                print(f"{Fore.YELLOW}[CLAVE] {candidate}\n")
                return candidate

    print(f"{Fore.RED}[X] No se encontró coincidencia en el diccionario.")
    return None


# ----------------------------
# Argumentos
# ----------------------------
def parse_arguments():
    parser = argparse.ArgumentParser(
        description="Cracker básico de hashes por diccionario"
    )
    parser.add_argument(
        "-a", "--algorithm",
        choices=["md5", "sha1", "sha256"],
        required=True,
        help="Algoritmo de hash (md5, sha1, sha256)"
    )
    parser.add_argument(
        "-t", "--target",
        required=True,
        help="Hash objetivo"
    )
    parser.add_argument(
        "-d", "--dictionary",
        required=True,
        help="Archivo de diccionario de contraseñas"
    )
    return parser.parse_args()


# ----------------------------
# Main
# ----------------------------
if __name__ == "__main__":
    args = parse_arguments()
    crack_hash(args.target, args.dictionary, args.algorithm)
