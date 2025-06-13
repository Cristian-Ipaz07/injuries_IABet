#!/bin/bash

# 📌 INJURIES_IABET - NBA INJURY DATA TRACKER
# Descripción: 
#   Script para extraer datos de lesiones de la NBA usando SportRadar API.
#   Guarda resultados en JSON y muestra resumen en terminal.

# 📦 DEPENDENCIAS
#   - Python 3.8+
#   - Pip
#   - requests (paquete Python)
#   - Virtualenv (opcional)

# 📂 ENTRADAS
#   - API Key válida de SportRadar (en scripts/main.py)
#   - Estructura de carpetas:
#     ./data/json/       # Para almacenar JSON
#     ./scripts/main.py  # Código principal

# 🖥️ SALIDAS
#   - Terminal: 
#     * Resumen de jugadores lesionados por equipo
#     * Estado de la operación (éxito/error)
#   - Archivos:
#     * data/json/nba_injuries_YYYY-MM-DD.json


# 🚀 USO BÁSICO
# 1. Configurar API Key en scripts/main.py
# 2. Ejecutar:
#    $ python scripts/main.py
