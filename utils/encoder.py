#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
encoder.py - Herramienta de encoding/decoding
---------------------------------------------
Este script permite convertir texto en varios formatos comunes:
Base64, Hexadecimal y ROT13. También permite decodificar.

Características:
- Encode y decode en Base64
- Encode y decode en Hexadecimal
- Encode y decode en ROT13
- Uso fácil desde línea de comandos

⚠️ Aviso legal:
Este script es únicamente para fines educativos en entornos
controlados. El uso contra sistemas de terceros sin autorización
es ilegal y contrario a la ética profesional.
"""

import argparse
import base64
import codecs
from colorama import Fore, Style, init

# Inicializar colorama
init(autoreset=True)


# ----------------------------
# Funciones de encoding/decoding
# ----------------------------
def encode_base64(text: str) -> str:
    return base64.b64encode(text.encode()).decode()

def decode_base64(text: str) -> str:
    return base64.b64decode(text.encode()).decode(errors="ignore")

def encode_hex(text: str) -> str:
    return text.encode().hex()

def decode_hex(text: str) -> str:
    return bytes.fromhex(text).decode(errors="ignore")

def encode_rot13(text: str) -> str:
    return codecs.encode(text, "rot_13")

def decode_rot13(text: str) -> str:
    return codecs.decode(text, "rot_13")


# ----------------------------
# Main
# ----------------------------
def main():
    parser = argparse.ArgumentParser(description="Herramienta de encoding/decoding")
    parser.add_argument("-m", "--mode", choices=["encode", "decode"], required=True, help="Modo: encode o decode")
    parser.add_argument("-a", "--algorithm", choices=["base64", "hex", "rot13"], required=True, help="Algoritmo")
    parser.add_argument("-t", "--text", required=True, help="Texto a procesar")
    args = parser.parse_args()

    result = ""
    if args.mode == "encode":
        if args.algorithm == "base64":
            result = encode_base64(args.text)
        elif args.algorithm == "hex":
            result = encode_hex(args.text)
        elif args.algorithm == "rot13":
            result = encode_rot13(args.text)
    elif args.mode == "decode":
        if args.algorithm == "base64":
            result = decode_base64(args.text)
        elif args.algorithm == "hex":
            result = decode_hex(args.text)
        elif args.algorithm == "rot13":
            result = decode_rot13(args.text)

    print(f"{Fore.GREEN}[{args.algorithm.upper()} - {args.mode.upper()}] {Fore.YELLOW}{result}")


if __name__ == "__main__":
    main()
