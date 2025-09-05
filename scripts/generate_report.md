```bash
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
generate_report.py - Generador de reporte de ataques
---------------------------------------------------
Analiza los logs de demo de ataque y defensa, generando un resumen
de intentos, éxitos y alertas por IP y usuario.

⚠️ Solo analiza logs locales de demo. No afecta otros archivos.
"""

import os
from collections import defaultdict
from colorama import Fore, init

# Inicializar colorama
init(autoreset=True)

# Logs por defecto
logs_to_analyze = [
    "honeypot_demo.log",
    "alerts_demo.log"
]

# Función para analizar logs
def analyze_logs(log_files):
    report_data = defaultdict(lambda: {"SUCCESS":0, "FAILED":0})
    
    for log_file in log_files:
        if not os.path.exists(log_file):
            print(f"{Fore.YELLOW}[!] Log no encontrado: {log_file}")
            continue
        
        with open(log_file, "r") as f:
            for line in f:
                if "dijo:" in line:
                    parts = line.strip().split()
                    ip_port = parts[2]
                    status = parts[-1].strip("[]")
                    report_data[ip_port][status] += 1
    
    return report_data

# Función para mostrar resumen
def display_report(report_data):
    print(f"{Fore.MAGENTA}\n=== RESUMEN DE ATAQUES ===\n")
    for ip_port, stats in report_data.items():
        print(f"{Fore.CYAN}Objetivo: {ip_port}")
        print(f"  {Fore.GREEN}Éxitos: {stats['SUCCESS']}")
        print(f"  {Fore.RED}Fallos: {stats['FAILED']}\n")

# Función para guardar reporte en archivo
def save_report(report_data, filename="report.txt"):
    with open(filename, "w") as f:
        f.write("=== RESUMEN DE ATAQUES ===\n\n")
        for ip_port, stats in report_data.items():
            f.write(f"Objetivo: {ip_port}\n")
            f.write(f"  Éxitos: {stats['SUCCESS']}\n")
            f.write(f"  Fallos: {stats['FAILED']}\n\n")
    print(f"{Fore.GREEN}[✓] Reporte guardado en {filename}")

# Main
if __name__ == "__main__":
    report = analyze_logs(logs_to_analyze)
    display_report(report)
    save_report(report)
```
---
## ⚡ Cómo usarlo
1. Ejecuta el script para analizar los logs por defecto:
Salida ejemplo en consola:
```
=== RESUMEN DE ATAQUES ===

Objetivo: 192.168.50.153:2222
  Éxitos: 3
  Fallos: 12

Objetivo: 192.168.50.101:22
  Éxitos: 1
  Fallos: 7
```
2. Se genera también un arhivo `report.txt` con el mismo resumen
