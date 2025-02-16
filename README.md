# 🚖 App-Taxímetro: Tu Taxímetro Digital Moderno y Completo 🚖

[![Build Status](https://github.com/Omarlsant/app-taximetro/actions/workflows/app-config.yml/badge.svg)](https://github.com/Omarlsant/app-taximetro/actions/workflows/app-config.yml)  <!-- ¡Insignia de GitHub Actions FUNCIONANDO! -->

## ✨ Descripción General

¡Bienvenido a **App-Taxímetro**, una solución de taxímetro digital completa, moderna y flexible!  Este proyecto no es solo un taxímetro; es una plataforma completa construida con las mejores prácticas de desarrollo y lista para el mundo real.  Calcula tarifas con precisión, ofrece interfaces para todo tipo de usuarios y está listo para escalar.

**Características Destacadas:**

*   **💰 Cálculo Preciso:** Configura tarifas base, tarifas por distancia/tiempo, recargos (nocturnos, festivos, etc.) ¡Todo personalizable!
*   **💻 Múltiples Interfaces:**
    *   **CLI:**  Control total desde la terminal.
    *   **GUI:** Interfaz gráfica intuitiva (desarrollada con Tkinter, o especifica el framework que usaste).
    *   **Web (React + Vite):**  Interfaz moderna, responsiva y accesible desde cualquier dispositivo.
*   **💾 Historial de Trayectos:**  Guarda automáticamente un registro detallado en formato JSON.
*   **⚙️ Configuración Sencilla:**  Modifica las tarifas en un archivo `config.json`  ¡Sin tocar código!
*   **📝 Logging Detallado:**  Rastrea eventos importantes para depuración y análisis.
*   **🧪 Pruebas Exhaustivas:**  Pruebas unitarias y de integración para garantizar la calidad y confiabilidad.
*   **🐳 Listo para Contenedores:**  Despliegue fácil con Docker y Docker Compose.
*   **🚀 CI/CD Integrado:**  Integración y despliegue continuos con GitHub Actions (automatización completa).

## 🏗️ Estructura del Proyecto

Una arquitectura bien organizada facilita la comprensión, el mantenimiento y la escalabilidad:
```
app-taximetro/
│
├── .gitignore # Archivos/carpetas ignorados por Git
├── main.py # Punto de entrada principal de la aplicación
├── pyproject.toml # Configuración del proyecto (dependencias, herramientas)
├── README.md # Este archivo
├── requirements.txt # Dependencias de Python
├── test_imports.py # Verifica que las importaciones funcionen correctamente
├── workflow.yml # Configuración de GitHub Actions (CI)
├── Dockerfile # Configuración para crear una imagen Docker
├── docker-compose.yml # Configuración para orquestar contenedores
│
├── src/ # Código fuente principal
│ ├── init.py
│ ├── cli.py # Interfaz de línea de comandos
│ ├── taximeter.py # Lógica central del taxímetro
│ ├── gui.py # Interfaz gráfica de usuario
│ └── utils.py # Funciones de utilidad
│
├── tests/ # Pruebas unitarias y de integración
│ ├── init.py
│ ├── test_cli.py # Pruebas para cli.py
│ ├── test_taximeter.py # Pruebas para taximeter.py
│ └── test_utils.py # Pruebas para utils.py
│
├── logs/ # Archivos de registro
│ └── taximeter.log
│
├── data/ # Datos y configuración
│ ├── history.json # Historial de trayectos
│ └── config.json # Configuración de tarifas
│
├── frontend/ # Código del frontend (React + Vite)
│ ├── .gitignore
│ ├── index.html
│ ├── vite.config.js
│ ├── package.json
│ ├── src/
│ │ ├── main.jsx
│ │ ├── App.jsx
│ │ ├── components/
│ │ ├── pages/
│ │ └── assets/
│ └── tests/
│
└── backend/ # Código del backend (opcional)
```


## 🚀 Instalación

1.  **Requisitos Previos:**
    *   Python 3.11+ (recomendado 3.11+)
    *   pip (gestor de paquetes de Python)
    *   Git (para clonar el repositorio)
    *   Node.js y npm (para el frontend)
    *   (Opcional) Docker y Docker Compose (para la contenerización)

2.  **Clonar el repositorio:**

    ```bash
    git clone https://github.com/omarlsant/app-taximetro.git  # Reemplaza
    cd app-taximetro
    ```

3.  **Instalar dependencias (Backend/Python):**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Instalar dependencias (Frontend):**

    ```bash
    cd frontend
    npm install
    cd ..
    ```

## ⚙️ Configuración

*   **Tarifas:** Edita el archivo `data/config.json` para ajustar las tarifas del taxímetro.  El archivo tiene la siguiente estructura (ejemplo):

    ```config.json
    {
        "stopped_rate": 0.02,
        "moving_rate": 0.05
    }
    ```

    *   `moving_rate`:  Tarifa base por iniciar el trayecto.
    *   `stopped_rate`: Tarifa por unidad de tiempo de espera (`time_unit`).
    *  `change_fee`:  Recargo adicional por trayectos nocturnos (puedes definir el horario en el código).
    *   `time_unit`:  Unidad de medida para `waiting_rate` ("second").

*   **Otras configuraciones:** Si tienes variables de entorno, constantes, etc., considera agregarlas a un archivo de configuración separado (ej., `src/config.py`) o usar una librería como `python-dotenv`.

## Uso

### 🕹️ Uso Interfaz de Línea de Comandos (CLI)

   * python main.py --cli 

### 🕹️ Interfaz de Gráfica de Usuario (GUI)

Ejecuta el programa principal:

   * python main.py 

## ✅ Ejecución de Pruebas

### Pruebas unitarias con unittest:

   * python -m unittest discover tests

## 🚀 CI/CD (Integración y Despliegue Continuos)

* El proyecto utiliza GitHub Actions para la integración continua (CI) y el despliegue continuo (CD). Las pruebas se ejecutan automáticamente en cada push y pull request, y la imagen de Docker se actualiza en Docker Hub.

## 🤝 Contribuciones

¡Las contribuciones son bienvenidas! Si tienes ideas, mejoras o correcciones, no dudes en abrir un issue o enviar un pull request.