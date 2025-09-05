# 🔴 Red Team – Operaciones Ofensivas

## 🌐 Introducción
El **Red Team** representa la mentalidad del adversario.  
Su función dentro del framework es **simular ataques reales** contra sistemas y servicios en un entorno de laboratorio, con el fin de poner a prueba las defensas del Blue Team.  

Los scripts en la carpeta `core/` han sido diseñados para reproducir técnicas comunes de ataque de forma controlada.

---

## 🎯 Objetivos del Red Team
1. Simular ataques frecuentes en escenarios empresariales.  
2. Generar tráfico malicioso para probar detecciones.  
3. Enseñar metodologías ofensivas de forma práctica.  
4. Documentar paso a paso los vectores de ataque.  

---

## ⚔️ Módulos ofensivos incluidos

### 1. Escaneo de red – `scanner.py`
- Basado en **socket scanning**.  
- Permite identificar puertos abiertos y servicios activos.  
- Emula la fase inicial de reconocimiento en un pentest.  

Ejemplo de ejecución:
```bash
python3 core/scanner.py -t 192.168.1.10 -p 20-1000
```
***📚 Casos prácticos***
*Caso 1 – Escaneo contra honeypot*

1. El atacante ejecuta `scanner.py`.

2. El honeypot del Blue Team (`honeypot_basic.py`) registra el intento.

*Caso 2 – Intentos de fuerza bruta*

1. `bruteforce_ssh.py` lanza múltiples credenciales.

2. El sistema defensivo activa alertas en `detect_scan.py`.

*Caso 3 – Conexión persistente*

1. Se lanza un `reverse_shell.py`.

2. `log_monitor.py` del Blue Team detecta actividad anómala.

***⚖️ Consideraciones***

Los ataques deben ejecutarse únicamente en laboratorios controlados.

No se incluyen exploits de día cero ni payloads avanzados.

Su propósito es educativo y formativo.
