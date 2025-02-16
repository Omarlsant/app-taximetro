# Taxímetro Digital:  App-Taximetro

[![CI](https://github.com/omarlsant/app-taximetro/workflows/workflow.yml/badge.svg)](https://github.com/omarlsant/app-taximetro/actions)

## Descripción

Este proyecto implementa un taxímetro digital completo con las siguientes características:

*   **Cálculo preciso de tarifas:**  Utiliza una configuración flexible para tarifas base, tarifas por distancia, tiempo de espera y recargos nocturnos/festivos.
*   **Interfaz de línea de comandos (CLI):**  Permite iniciar, detener y consultar el taxímetro desde la terminal.
*   **Interfaz gráfica de usuario (GUI):**  Proporciona una experiencia de usuario intuitiva con botones y visualización en tiempo real. (Implementada con `gui.py`,  asume un framework, se puede especificar si es Tkinter, PyQt, etc.)
*   **Interfaz web (Frontend):**  Desarrollada con React (usando Vite) para una experiencia moderna y accesible desde cualquier dispositivo.
*   **(Opcional) Backend:**  Estructura preparada para un posible backend (si decides implementar lógica de servidor, API, etc.).
*   **Registro histórico:**  Guarda un historial de los trayectos en formato JSON (`history.json`).
*   **Configuración personalizable:**  Las tarifas se pueden configurar fácilmente en `data/config.json`.
*   **Logging:**  Registra eventos importantes en `logs/taximeter.log` para depuración y seguimiento.
*   **Pruebas unitarias y de integración:**  Cobertura de pruebas exhaustiva para garantizar la calidad del código.
*   **Contenedorización:**  Listo para ser desplegado en contenedores Docker usando `Dockerfile` y `docker-compose.yml`.
*   **Integración Continua (CI):** Configurado con GitHub Actions (`workflow.yml`) para automatizar pruebas y validaciones.

## Estructura del Proyecto

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


## Instalación

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

## Configuración

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

### Interfaz de Línea de Comandos (CLI)

   * python main.py --cli 

### Interfaz de Gráfica de Usuario (GUI)

Ejecuta el programa principal:

   * python main.py 

## Ejecución de pruebas

### Pruebas unitarias con unittest:

   * python -m unittest discover tests

## Integración Continua (CI) y Despliegue Continuo (CD)

* El proyecto utiliza GitHub Actions para la integración continua (CI) y el despliegue continuo (CD). Las pruebas se ejecutan automáticamente en cada push y pull request, y la imagen de Docker se actualiza en Docker Hub.