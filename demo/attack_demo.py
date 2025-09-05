# Demo de Ataque Simulado (`attack_demo.py`)

Este script simula un ataque a un host de laboratorio, generando logs que luego pueden ser usados por el IDS y el monitor para demostraciones educativas.

## Características

- Escaneo de puertos simulados.
- Ataque de fuerza bruta SSH simulado.
- Generación de log `honeypot_demo.log`.
- Totalmente reproducible sin máquinas virtuales ni servicios reales.

> ⚠️ Uso educativo: No ataca hosts reales.

## Código

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
attack_demo.py - Demo de ataque simulado
---------------------------------------
Este script simula un ataque a un host con:
- Escaneo de puertos
- Fuerza bruta SSH

Genera un log simulado honeypot_demo.log que puede ser
analizado por IDS y monitor para demostración.

⚠️ Aviso legal:
Modo demo educativo. No ataca hosts reales.
"""

import random
import time
from datetime import datetime
from colorama import Fore, Style, init

# Inicializar colorama
init(autoreset=True)

# Configuración de simulación
target_ip = "192.168.50.153"
puertos_simulados = [22, 80, 443, 8080, 2222]  # Puertos abiertos simulados
user_list = ["root", "admin", "test"]
pass_list = ["123456", "toor", "admin123"]
logfile = "honeypot_demo.log"

# Función de log simulado
def write_log(message: str):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(logfile, "a") as f:
        f.write(f"{timestamp} - {message}\n")

# Simulación de scanner
def simulate_scanner():
    print(f"{Fore.GREEN}[+] Simulando escaneo de {target_ip}...\n")
    for port in range(20, 1025):
        time.sleep(0.01)
        if port in puertos_simulados:
            print(f"{Fore.CYAN}[OPEN] Puerto {port} abierto")
            write_log(f"Puerto abierto detectado: {port}")

# Simulación de fuerza bruta
def simulate_brute_force():
    print(f"\n{Fore.GREEN}[+] Simulando ataque de fuerza bruta contra {target_ip}:2222\n")
    for user in user_list:
        for pwd in pass_list:
            time.sleep(0.05)
            success = random.choice([False, False, True])
            if success:
                print(f"{Fore.YELLOW}[SUCCESS] Usuario: {user} | Contraseña: {pwd}")
                write_log(f"{target_ip}:2222 dijo: {user}:{pwd} [SUCCESS]")
                return
            else:
                print(f"{Fore.RED}[FAILED] {user}:{pwd}")
                write_log(f"{target_ip}:2222 dijo: {user}:{pwd} [FAILED]")

# Main
if __name__ == "__main__":
    print(f"{Fore.MAGENTA}[✓] Iniciando demo de ataque simulado...\n")
    simulate_scanner()
    simulate_brute_force()
    print(f"\n{Fore.MAGENTA}[✓] Demo completada. Log generado en {logfile}")
