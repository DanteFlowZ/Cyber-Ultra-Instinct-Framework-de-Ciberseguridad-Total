```bash
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
setup_env.py - Configuración del entorno de demo
------------------------------------------------
Este script prepara el entorno para las demos de ataque y defensa:
- Instala dependencias necesarias
- Crea logs vacíos
- Comprueba versiones de Python y paquetes

⚠️ Solo afecta entorno local de demo.
"""

import os
import sys
import subprocess
from colorama import Fore, init

# Inicializar colorama
init(autoreset=True)

# Logs por defecto
logs_to_create = [
    "honeypot_demo.log",
    "alerts_demo.log"
]

# Dependencias necesarias
dependencies = [
    "colorama"
]

# ----------------------------
# Función para instalar dependencias
# ----------------------------
def install_dependencies():
    print(f"{Fore.GREEN}[+] Instalando dependencias...")
    for package in dependencies:
        subprocess.run([sys.executable, "-m", "pip", "install", package])
    print(f"{Fore.GREEN}[✓] Dependencias instaladas.\n")

# ----------------------------
# Función para crear logs vacíos
# ----------------------------
def create_logs():
    print(f"{Fore.GREEN}[+] Creando logs vacíos...")
    for log in logs_to_create:
        with open(log, "w") as f:
            f.truncate(0)
        print(f"{Fore.CYAN}[✓] Log creado: {log}")
    print("")

# ----------------------------
# Main
# ----------------------------
if __name__ == "__main__":
    # Comprobar versión de Python
    if sys.version_info < (3, 8):
        print(f"{Fore.RED}[!] Se recomienda Python 3.8 o superior")
    
    install_dependencies()
    create_logs()
    print(f"{Fore.MAGENTA}[✓] Entorno de demo listo para ejecutar scripts.")
```
---
## ⚡ Cómo usarlo
1. Ejecuta el script para preparar el entorno
```bash
python3 scripts/setup_env.py
```
2. Se instalarán las dependencias y se crearán los logs vacíos.
Salida ejemplo:
```
[+] Instalando dependencias...
[✓] Dependencias instaladas.

[+] Creando logs vacíos...
[✓] Log creado: honeypot_demo.log
[✓] Log creado: alerts_demo.log

[✓] Entorno de demo listo para ejecutar scripts.
```


