# 🏗️ Arquitectura del Framework

## 🌐 Visión general
El **Framework Cyber Ultra Instinct** se organiza como un sistema modular en el que cada componente cumple un rol específico.  
La idea central es **simular ataques y defensas en un entorno controlado**, de forma que se pueda estudiar el comportamiento del adversario y probar contramedidas.

La arquitectura se divide en **tres capas principales**:
1. **Capa ofensiva (Red Team)** → scripts y técnicas de ataque.
2. **Capa defensiva (Blue Team)** → detección, honeypots, alertas.
3. **Capa de automatización** → despliegue y orquestación de entornos.

---

## 📂 Estructura de directorios

```plaintext
cyber-ultrainstinct/
│
├── core/              # Red Team (ataques y explotación)
│   ├── scanner.py
│   ├── bruteforce_ssh.py
│   └── reverse_shell.py
│
├── defense/           # Blue Team (defensa y monitorización)
│   ├── honeypot_basic.py
│   ├── detect_scan.py
│   └── log_monitor.py
│
├── automation/        # Infraestructura como código
│   ├── ansible_playbook.yml
│   └── terraform_setup.tf
│
├── docs/              # Documentación académica y técnica
├── tests/             # Validación de scripts
└── assets/            # Diagramas y recursos visuales
