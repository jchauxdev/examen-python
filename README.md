# 🕵️‍♂️ CTF Python: Extracción de Datos (Escape Room Educativo)

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red.svg)
![Education](https://img.shields.io/badge/Tipo-Evaluaci%C3%B3n_Gamificada-success.svg)

Una aplicación web interactiva diseñada para evaluar conocimientos de procesamiento de datos en Python a través de una dinámica de "Capture The Flag" (CTF) o "Escape Room". 

Los estudiantes deben resolver problemas lógicos complejos utilizando sus propios entornos de desarrollo (IDE) y validar sus resultados en esta plataforma para avanzar de nivel.

## ✨ Características Principales

* **🎲 Banco Aleatorio de Preguntas:** Cuenta con un banco de 15 problemas avanzados. A cada estudiante se le asignan 10 retos aleatorios, mitigando el riesgo de copia en el aula.
* **🛡️ Diseño Anti-IA (Anti-Cheat):** Las preguntas están estructuradas para entregar datos en bruto y solicitar la extracción de un valor matemático específico. Esto obliga al estudiante a programar la lógica de extracción (ETL), haciéndolo resistente a la simple copia en modelos de IA generativa.
* **✅ Validación Inteligente:** El sistema tolera variaciones menores en las respuestas (como el uso de comas o puntos para decimales, o diferencias de redondeo `rel_tol=1e-3`).
* **🎓 Certificado de Aprobación:** Al finalizar los 10 niveles, la aplicación genera un *Token de Certificación* (archivo `.txt`) descargable con el nombre del estudiante como evidencia de la evaluación.

## 🧠 Temas Evaluados

Esta evaluación cubre los fundamentos del Procesamiento de Datos para Inteligencia Artificial:
* Manipulación de **Strings** (`split`, `replace`, indexación).
* Estructuras de control (`for`, `while`, `if/elif/else`).
* Estructuras de datos (**Listas**, **Tuplas**, **Diccionarios** y diccionarios anidados).
* Tipado y Casting (`int`, `float`, `str`).
* Operaciones matemáticas (sumatorias, promedios, librería `math`).

---

## ☁️ Despliegue en Streamlit Community Cloud (Gratis)**

Para que tus estudiantes puedan acceder a la evaluación desde cualquier navegador sin instalar nada, la mejor opción es alojar la aplicación en Streamlit Community Cloud. Es un proceso gratuito y toma menos de 5 minutos.

### Paso 1: Preparar tu repositorio en GitHub
1. Entra a [GitHub](https://github.com/) e inicia sesión (o crea una cuenta si no tienes una).
2. Crea un nuevo repositorio público. Puedes llamarlo `ctf-python-evaluacion`.
3. Sube a este repositorio dos archivos fundamentales:
   * `app.py`: El archivo con todo el código de la aplicación.
   * `requirements.txt`: Un archivo de texto que debe contener únicamente la palabra `streamlit`. Esto le dice al servidor qué librería necesita instalar.

### Paso 2: Conectar con Streamlit
1. Entra a [Streamlit Community Cloud](https://share.streamlit.io/) y haz clic en **"Sign up"** o **"Continue with GitHub"**.
2. Otorga los permisos necesarios para que Streamlit pueda leer tus repositorios públicos de GitHub.

### Paso 3: Desplegar la aplicación
1. Una vez dentro del panel de Streamlit, haz clic en el botón azul de la esquina superior derecha que dice **"New app"**.
2. Si te pregunta, selecciona la opción **"Deploy an app"** o **"Use existing repo"**.
3. Completa el formulario de despliegue:
   * **Repository:** Escribe el nombre de tu repositorio (ej. `tu-usuario/ctf-python-evaluacion`).
   * **Branch:** Normalmente es `main` o `master`.
   * **Main file path:** Escribe `app.py`.
   * **App URL (Opcional):** Puedes personalizar el link que se generará (ej. `evaluacion-sena-2026`).
4. Haz clic en el botón **"Deploy!"**.

### Paso 4: ¡Listo para la clase!
* Verás una pantalla de carga con "globos" mientras el servidor instala Python y levanta tu aplicación. Esto toma alrededor de 1 a 2 minutos la primera vez.
* Una vez finalizado, la aplicación aparecerá en tu pantalla.
* Comparte la URL pública con tus estudiantes (ej. https://tu-app.streamlit.app).
* Para ti como instructor: Ingresa a https://tu-app.streamlit.app/?admin=true para activar tu panel de control oculto.

---

## 🚀 Instalación y Ejecución Local (Recomendado para el Aula)

Ejecutar la aplicación localmente convierte la computadora del instructor en el servidor del examen. Esto garantiza estabilidad total, evita caídas por servidores externos y no requiere internet de alta velocidad en el salón.

### Paso 1: Preparar el Entorno
**Clona este repositorio:**

    git clone https://github.com/jchauxdev/examen-python.git

Abre una terminal (CMD, PowerShell o la terminal de VS Code) y navega hasta esa carpeta:

    cd ruta_repo

### Paso 2: Instalar Dependencias
Asegúrate de tener Python instalado. Luego, instala la librería requerida:

    pip install -r requeriments.txt

### Paso 3: Iniciar el Servidor del Examen
Ejecuta el siguiente comando para levantar la aplicación:

    streamlit run app.py

###  Paso 4: ¿Cómo se conectan los Estudiantes vs El Instructor?
Al ejecutar el comando, la terminal te mostrará dos URLs (Local y Network). La clave está en cómo usarlas:

* 👨‍🎓 Para los Aprendices (Acceso al Examen): Entrégales la Network URL limpia (ej. http://192.168.x.x:8501). Ellos verán la pantalla de espera sin ningún panel de control.

* 👨‍🏫 Para el Instructor (Panel de Control): Usa la Local URL y agrégale el parámetro secreto /?admin=true al final. Quedará así: http://localhost:8501/?admin=true. Al usar este enlace, te aparecerá el panel lateral para ingresar la contraseña y habilitar la prueba.

⚠️ IMPORTANTE: Para que la Network URL funcione, tanto el servidor (tu PC) como los aprendices deben estar conectados a la misma red Wi-Fi o LAN.

