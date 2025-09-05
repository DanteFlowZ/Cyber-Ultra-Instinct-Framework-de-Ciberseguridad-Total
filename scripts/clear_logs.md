```bash
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
clear_logs.py - Limpieza de logs de demo
---------------------------------------
Este script permite borrar o vaciar logs generados por las demos
de ataque y defensa, dejando el entorno listo para nuevas pruebas.

⚠️ Solo borra logs locales de demo. No afecta otros archivos.
"""

import os
import argparse
from colorama import Fore, init

# Inicializar colorama
init(autoreset=True)

# Logs por defecto
default_logs = [
    "honeypot_demo.log",
    "alerts_demo.log"
]

# ----------------------------
# Función limpiar logs
# ----------------------------
def clear_logs(logs):
    for log in logs:
        if os.path.exists(log):
            with open(log, "w") as f:
                f.truncate(0)
            print(f"{Fore.GREEN}[✓] Log limpiado: {log}")
        else:
            print(f"{Fore.YELLOW}[!] Log no encontrado: {log}")

# ----------------------------
# Argumentos
# ----------------------------
def parse_arguments():
    parser = argparse.ArgumentParser(description="Limpieza de logs de demo")
    parser.add_argument(
        "-l", "--logs",
        nargs="+",
        help="Lista de logs a limpiar (por defecto todos los logs de demo)"
    )
    return parser.parse_args()

# ----------------------------
# Main
# ----------------------------
if __name__ == "__main__":
    args = parse_arguments()
    logs_to_clear = args.logs if args.logs else default_logs
    clear_logs(logs_to_clear)

```

---

## ⚡ Cómo usarlo
1. Limpiar todos los logs por defecto:
```bash
python3 scripts/clear_logs.py
```
Salida ejemplo
``` less
[✓] Log limpiado: honeypot_demo.log
[✓] Log limpiado: alerts_demo.log
```
2. Limpiar logs específicos:
```
python3 scripts/clear_logs.py -l honeypot_demo.log
```
Salida ejemplo:
```
[✓] Log limpiado: honeypot_demo.log
```
