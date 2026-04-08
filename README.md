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

## 🚀 Instalación y Ejecución Local

Si deseas probar o modificar la aplicación en tu propia máquina, sigue estos pasos:

1. **Clona este repositorio:**
   ```bash
   git clone [https://github.com/jchauxdev/examen-python.git](https://github.com/jchauxdev/examen-python.git)
   cd TU_REPOSITORIO