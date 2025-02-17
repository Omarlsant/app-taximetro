# App-Taxímetro (Frontend): Tu Taxímetro Digital en la Web 🚖✨

[![GitHub Pages](https://omarlsant.github.io/taximeter-app/)](Reemplaza con tu link de GitHub Pages)
[![React](https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB)](https://reactjs.org/)
[![Vite](https://img.shields.io/badge/Vite-B73BFE?style=for-the-badge&logo=vite&logoColor=FFD700)](https://vitejs.dev/)

**¿Qué es esto?**

Este es el frontend web de App-Taxímetro, un taxímetro digital completo y moderno.  Construido con [React](https://reactjs.org/) y [Vite](https://vitejs.dev/), ofrece una interfaz intuitiva y responsiva para calcular tarifas de taxi desde cualquier dispositivo con un navegador web.

**Características Clave:**

*   **Interfaz Moderna:** 💻 Diseño limpio y fácil de usar, adaptable a pantallas de todos los tamaños (¡responsive!).
*   **Cálculo en Tiempo Real:** ⏱️ Observa cómo la tarifa se actualiza a medida que ingresas la distancia y el tiempo (o mientras el taxímetro está en marcha).
*   **Configuración Sencilla:** ⚙️ Las tarifas se configuran desde un archivo `config.json`.
*   **Desplegado con GitHub Pages:** 🚀 Acceso rápido y gratuito, ¡sin necesidad de configurar servidores!

**Tecnologías Usadas:**

*   **React:** ⚛️ Biblioteca de JavaScript para construir interfaces de usuario interactivas.
*   **Vite:** ⚡️ Herramienta de desarrollo frontend ultrarrápida (compilación, recarga en caliente, etc.).
*   **GitHub Pages:** 🌐 Servicio de hosting estático de GitHub (fácil despliegue).

**Estructura del Proyecto (simplificada):**
```
app-taximetro/
│
│
└── client-app-taximetro/               # Directorio para el código del front-end
    ├── eslint.config.js                # Archivo de configuración para ESLint
    ├── index.html                      # Archivo HTML principal
    ├── vite.config.js                  # Archivo de configuración de Vite
    ├── package.json                    # Archivo de configuración de NPM
    ├── package-lock.json               # se crea automáticamente para registrar las versiones exactas de cada dependencia
    └── src/                            # Código fuente del front-end
        ├── assets/                     # Archivo principal de React
        ├── components/                 # Componente principal de la aplicación
        ├── layout/                     # Directorio para los componentes de React
        ├── pages/                      # Directorio para las páginas de la aplicación
        ├── router                      # Lógica para la navegación entre las diferentes páginas (enrutamiento).
        ├── index.css                   # Hoja de estilos CSS globales para la aplicación.
        └── main.jsx                    # El punto de entrada principal de la aplicación React
```

**¿Cómo empezar (si quieres contribuir o ejecutar localmente)?**

1.  **Clona el Repositorio:** ⬇️ (si aún no lo has hecho):

    ```bash
    git clone https://github.com/omarlsant/app-taximetro.git  # Reemplaza con la URL correcta
    cd app-taximetro/frontend
    ```

2.  **Instala Dependencias:** 📦

    ```bash
    npm install
    ```

3.  **Ejecuta en Modo Desarrollo:** ▶️

    ```bash
    npm run dev
    ```

    Esto abrirá la aplicación en tu navegador (normalmente en `http://localhost:5173` o un puerto similar).  ¡Verás los cambios reflejados casi instantáneamente!

**¡Contribuye!**

¿Tienes ideas para mejorar la interfaz, corregir errores o añadir nuevas funciones?  ¡Abre un *issue* o envía un *pull request*!  Toda contribución es bienvenida. 💬

**Notas Importantes:**

*   **Hosting:** 🌐 Esta versión está *solo* enfocada en el frontend estático (HTML, CSS, JavaScript). Si quieres un backend completo (base de datos, lógica de servidor), revisa el README principal del proyecto App-Taxímetro.
*   **Configuración de Tarifas:** ⚙️ Se realiza mediante el archivo `config.json`.
*   **GitHub Pages:** ✅ Asegúrate de configurar correctamente tu repositorio para GitHub Pages (rama `gh-pages` o la configuración de *custom domain*).  Consulta la documentación de GitHub Pages para más detalles.
*   **Backend:** 🔗 Si tienes el backend desplegado, recuerda configurar las variables de entorno, o la URL del backend en el frontend.

**En Resumen:**

Este README se centra en el frontend de la app.  Si quieres saber cómo funciona de manera completa (con backend en Python, integración continua, etc.), te sugiero ver el README principal del proyecto. En general es una aplicación con:
* Backend en Python 🐍
* Frontend en React + Vite ⚛️⚡️
* CI/CD (GitHub Actions) 🔄
* Despliegue fácil (Docker y GitHub Pages) 🚀🌐
* ¡Y mucho más! 💪