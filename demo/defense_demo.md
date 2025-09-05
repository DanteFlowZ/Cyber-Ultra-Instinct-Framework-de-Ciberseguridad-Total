```phyton
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
defense_demo.py - Demo de defensa simulado
------------------------------------------
Combina honeypot, IDS y monitor en modo demo.
Genera logs de ataques simulados para análisis.
"""

import time
import random
from datetime import datetime
from colorama import Fore, Style, init
from collections import defaultdict

# Inicializar colorama
init(autoreset=True)

# Configuración
logfile = "honeypot_demo.log"
threshold = 3  # intentos para alerta
window = 60  # segundos
target_ip = "192.168.50.153"

# Variables IDS
attempts = defaultdict(list)

# Función para generar log simulado de ataques
def simulate_honeypot_activity():
    users = ["root", "admin", "test"]
    passwords = ["123456", "toor", "admin123"]
    ports_open = [22, 80, 443, 2222]
    
    print(f"{Fore.GREEN}[+] Simulando actividad de honeypot...\n")
    
    for _ in range(20):
        ip = f"192.168.50.{random.randint(1,254)}"
        user = random.choice(users)
        pwd = random.choice(passwords)
        port = random.choice(ports_open)
        success = random.choice([False, False, True])
        result = "SUCCESS" if success else "FAILED"
        
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_line = f"{timestamp} - {ip}:{port} dijo: {user}:{pwd} [{result}]"
        
        # Guardar en log
        with open(logfile, "a") as f:
            f.write(log_line + "\n")
        
        print(f"{Fore.CYAN}{log_line}")
        time.sleep(0.1)  # simular tiempo entre intentos

# Función IDS simulada
def run_ids_simulation():
    print(f"\n{Fore.YELLOW}[!] Analizando logs con IDS simulado...\n")
    
    with open(logfile, "r") as f:
        for line in f:
            ip = line.split()[2].split(":")[0]
            timestamp = datetime.now()
            attempts[ip].append(timestamp)
            # limpiar intentos viejos
            attempts[ip] = [t for t in attempts[ip] if t > timestamp - timedelta(seconds=window)]
            if len(attempts[ip]) >= threshold:
                alert_msg = f"[ALERTA] Posible ataque de fuerza bruta desde {ip}"
                print(f"{Fore.RED}{Style.BRIGHT}{alert_msg}")
                attempts[ip] = []

# Main demo
if __name__ == "__main__":
    print(f"{Fore.MAGENTA}[✓] Iniciando demo de defensa simulada...\n")
    simulate_honeypot_activity()
    run_ids_simulation()
    print(f"\n{Fore.MAGENTA}[✓] Demo de defensa completada. Log en {logfile}")
```
---
## ⚡ Cómo usarlo
1. Ejecuta la demo de defensa:
```bash
python3 defense_demo.py
```
2. Se genera un log `honeypot_demo.log` con actividad simulada.
3. Puedes abrir `monitor.py` para verlo en tiempo real:
```bash
python3 monitor.py -l honeypot_demo.log
```
4. El IDS simulado detectará IPs con múltiples intentos y mostrará **alertas en rojo**
