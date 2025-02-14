import json
import os
from datetime import datetime

DEFAULT_CONFIG = {
    "stopped_rate": 0.02,
    "moving_rate": 0.05
}

def load_config(config_path="data/config.json"):
    try:
        with open(config_path, 'r', encoding='utf-8') as f:  # Usa encoding='utf-8' al leer
            config = json.load(f)
            if not all(key in config for key in ["stopped_rate", "moving_rate"]):
                raise ValueError("Archivo de configuración incompleto.")
            return config
    except (FileNotFoundError, json.JSONDecodeError, ValueError) as e:
        print(f"Error al cargar config: {e}. Usando valores predeterminados.")
        return DEFAULT_CONFIG

def update_config(stopped_rate, moving_rate, config_path="data/config.json"):
    config = {"stopped_rate": stopped_rate, "moving_rate": moving_rate}
    try:
        with open(config_path, 'w', encoding='utf-8') as f:  # Usa encoding='utf-8' al escribir
            json.dump(config, f, indent=4)
    except Exception as e:
        print(f"Error al guardar config: {e}")

def save_history(fare):
    now = datetime.now()
    timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
    try:
        with open("data/history.txt", "a", encoding='utf-8') as f:  # ¡Usa encoding='utf-8'!
            f.write(f"Fecha y Hora: {timestamp}, Tarifa: {fare:.2f}€\n")
    except Exception as e:
        print(f"Error al guardar en el historial: {e}")

if not os.path.exists("logs/"):
    os.makedirs("logs/")
if not os.path.exists("data/"):
    os.makedirs("data/")