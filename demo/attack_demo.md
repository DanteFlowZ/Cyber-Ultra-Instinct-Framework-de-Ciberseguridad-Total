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

# ----------------------------
# Configuración de simulación
# ----------------------------
target_ip = "192.168.50.153"
puertos_simulados = [22, 80, 443, 8080, 2222]  # Puertos abiertos simulados
user_list = ["root", "admin", "test"]
pass_list = ["123456", "toor", "admin123"]
logfile = "honeypot_demo.log"

# ----------------------------
# Función de log simulado
# ----------------------------
def write_log(message: str):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(logfile, "a") as f:
        f.write(f"{timestamp} - {message}\n")


# ----------------------------
# Simulación de scanner
# ----------------------------
def simulate_scanner():
    print(f"{Fore.GREEN}[+] Simulando escaneo de {target_ip}...\n")
    for port in range(20, 1025):
        time.sleep(0.01)  # velocidad de escaneo
        if port in puertos_simulados:
            print(f"{Fore.CYAN}[OPEN] Puerto {port} abierto")
            write_log(f"Puerto abierto detectado: {port}")


# ----------------------------
# Simulación de fuerza bruta
# ----------------------------
def simulate_brute_force():
    print(f"\n{Fore.GREEN}[+] Simulando ataque de fuerza bruta contra {target_ip}:2222\n")
    for user in user_list:
        for pwd in pass_list:
            time.sleep(0.05)
            success = random.choice([False, False, True])  # aleatorio: 1/3 éxito
            if success:
                print(f"{Fore.YELLOW}[SUCCESS] Usuario: {user} | Contraseña: {pwd}")
                write_log(f"{target_ip}:2222 dijo: {user}:{pwd} [SUCCESS]")
                return
            else:
                print(f"{Fore.RED}[FAILED] {user}:{pwd}")
                write_log(f"{target_ip}:2222 dijo: {user}:{pwd} [FAILED]")


# ----------------------------
# Main
# ----------------------------
if __name__ == "__main__":
    print(f"{Fore.MAGENTA}[✓] Iniciando demo de ataque simulado...\n")
    simulate_scanner()
    simulate_brute_force()
    print(f"\n{Fore.MAGENTA}[✓] Demo completada. Log generado en {logfile}")
```

## ⚡ Cómo usarlo

1. Ejecuta la demo:
   ```bash
   python3 attack_demo.py
   ```
2. Se genera un log `honeypot_demo.log` con entradas simuladas como si fueran ataques reales
3. Luego puedes abrir `monitor.py` apuntando a este log:
   ```bash
   python3 monitor.py -l honeypot_demo.log
   ```
4. Si quieres, también puedes ejecutar ´ids.py´ sobre el log para ver alertas simuladas:
   ```bash
   python3 ids.py -l honeypot_demo.log -t 3 -w 60
    ```
   🔥 Con esto tienes una demo completa reproducible en cualquier máquina.
