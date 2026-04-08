import streamlit as st
import math
import random

# --- CONFIGURACIÓN DE LA PÁGINA ---
st.set_page_config(page_title="CTF Python: Nivel Dios", page_icon="💻", layout="centered")

# --- BANCO DE PREGUNTAS (15 Preguntas Complejas) ---
banco_preguntas = [
    {
        "titulo": "Análisis de Logs Corruptos",
        "contexto": 'Se recibe la siguiente trama de un servidor:\n`trama = "ERR_404:12;WARN_200:5;ERR_500:8;INFO_100:20;ERR_403:3"`',
        "mision": "Extrae el número de instancias (el número después de los dos puntos) ÚNICAMENTE de los registros que contengan la palabra 'ERR'. Suma esos valores.",
        "respuesta": 23
    },
    {
        "titulo": "Filtro de Dataset Financiero",
        "contexto": 'Tienes la siguiente lista de tuplas (Nombre, Edad, Salario):\n`datos = [("Juan", 25, 4500), ("Ana", 30, 5000), ("Luis", 22, 3000), ("Maria", 28, 6000)]`',
        "mision": "Filtra únicamente a los usuarios mayores de 24 años. Calcula el promedio de sus salarios y redondéalo a 2 decimales.",
        "respuesta": 5166.67
    },
    {
        "titulo": "Matriz de Pesos Neuronales",
        "contexto": 'Una capa oculta de una IA tiene esta matriz de pesos (lista de listas):\n`matriz = [[10, 2, 5], [4, 15, 6], [8, 8, 20]]`',
        "mision": "Calcula la suma de la diagonal principal (10, 15, 20) y la suma de la diagonal secundaria (5, 15, 8). ¿Cuál es la diferencia absoluta (positiva) entre ambas sumas?",
        "respuesta": 17
    },
    {
        "titulo": "Procesamiento de Cadenas de ADN",
        "contexto": 'Secuencia extraída:\n`dna = "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"`',
        "mision": "Cuenta cuántas veces aparece la letra 'C' y cuántas veces aparece la letra 'G'. Multiplica ambos resultados.",
        "respuesta": 204
    },
    {
        "titulo": "Distancia Máxima en Clústeres",
        "contexto": 'Coordenadas de nodos detectados:\n`nodos = [(0,0), (3,4), (5,12), (8,15)]`',
        "mision": "Calcula la distancia euclidiana entre el primer nodo (0,0) y el último nodo (8,15). Usa math.sqrt y da el resultado como un número entero.",
        "respuesta": 17
    },
    {
        "titulo": "Agrupamiento Inverso (Diccionarios)",
        "contexto": 'Mapeo de usuarios a clústeres:\n`d = {"u1": 1, "u2": 2, "u3": 1, "u4": 3, "u5": 2}`',
        "mision": "Si inviertes el diccionario para saber cuántos usuarios tiene cada clúster, ¿Cuántos clústeres tienen EXACTAMENTE 2 usuarios asignados?",
        "respuesta": 2
    },
    {
        "titulo": "Simulación: El Rebote del Gradiente",
        "contexto": 'Un valor inicia en 100.0. En cada iteración de un ciclo `while`, el valor se multiplica por 0.75.',
        "mision": "¿Cuántas iteraciones (ciclos) completas tienen que pasar para que el valor sea estrictamente menor a 1.0?",
        "respuesta": 17
    },
    {
        "titulo": "Cifrado Cíclico ASCII",
        "contexto": 'Mensaje a procesar: `msg = "DATA"`',
        "mision": "Recorre el string. Al código ASCII (usando `ord()`) de la primera letra súmale 1, a la segunda súmale 2, a la tercera 3, y a la cuarta 4. Suma los 4 nuevos valores numéricos obtenidos.",
        "respuesta": 292
    },
    {
        "titulo": "Optimización de Inventario",
        "contexto": 'Diccionario de stock actual vs mínimo requerido:\n`inv = {"A": [10, 15], "B": [20, 18], "C": [5, 20], "D": [30, 30]}`\n*(El índice 0 es el stock, el índice 1 es el mínimo).*',
        "mision": "Itera el diccionario. Si el stock es menor al mínimo, calcula cuántas unidades faltan. Suma todas las unidades faltantes de todo el inventario.",
        "respuesta": 20
    },
    {
        "titulo": "La Conjetura del Analista",
        "contexto": 'Iniciamos con la semilla `n = 27`.',
        "mision": "Aplica un ciclo while que termine cuando n sea 1. Si n es par, divídelo entre 2 (división entera `//`). Si es impar, multiplícalo por 3 y súmale 1. ¿Cuántos pasos (iteraciones) toma llegar a 1?",
        "respuesta": 111
    },
    {
        "titulo": "Limpieza de Textos Atípicos",
        "contexto": 'Frase sucia:\n`frase = "  PytH0n eS un lEnguAj3 d3 I.A.   "`',
        "mision": "1. Elimina los espacios al inicio y al final. 2. Convierte todo a minúsculas. 3. Cuenta cuántas vocales 'e' (normales, sin tilde) quedaron en la frase final.",
        "respuesta": 2
    },
    {
        "titulo": "Búsqueda de Primos en Rango",
        "contexto": 'Necesitamos la suma de ciertos números de puerto.',
        "mision": "Usando ciclos `for` anidados (o lógica matemática), encuentra y suma TODOS los números primos positivos que sean estrictamente menores a 50.",
        "respuesta": 328
    },
    {
        "titulo": "Diccionario de Frecuencias Anidadas",
        "contexto": 'Transacciones por sucursal:\n`ventas = {"Sur": {"A": 120, "B": 50}, "Norte": {"A": 80, "C": 110}, "Este": {"B": 40, "C": 60}}`',
        "mision": "Itera el diccionario anidado para encontrar el total de ventas (suma) EXCLUSIVAMENTE del producto 'C' en todas las sucursales.",
        "respuesta": 170
    },
    {
        "titulo": "Filtrado de Tuplas Condicionales",
        "contexto": 'Lista de modelos y precisiones:\n`modelos = [("M1", 0.85), ("M2", 0.92), ("M3", 0.78), ("M4", 0.95)]`',
        "mision": "Multiplica por 100 las precisiones para hacerlas enteros. Suma las precisiones numéricas (ya como enteros) SOLO de los modelos cuya precisión sea mayor o igual a 90.",
        "respuesta": 187
    },
    {
        "titulo": "Detección de Subcadenas Repetidas",
        "contexto": 'Log binario:\n`binario = "101100101010011010101110"`',
        "mision": "Usando el método de conteo de strings, ¿cuántas veces aparece el patrón exacto '101' en esta cadena? (Nota: asume el comportamiento normal de .count(), sin solapamientos).",
        "respuesta": 4
    }
]

# --- INICIALIZACIÓN DEL ESTADO ---
# Esto garantiza que las preguntas se elijan 1 sola vez por estudiante
if 'preguntas_estudiante' not in st.session_state:
    st.session_state.preguntas_estudiante = random.sample(banco_preguntas, 10)
    st.session_state.indice_actual = 0
    st.session_state.respuestas_correctas = 0

# --- FUNCIÓN DE VALIDACIÓN ---
def verificar_respuesta(respuesta_usuario, respuesta_correcta):
    if respuesta_usuario == "": return False
    try:
        val_usuario = float(respuesta_usuario.replace(',', '.').strip())
        val_correcta = float(respuesta_correcta)
        return math.isclose(val_usuario, val_correcta, rel_tol=1e-3)
    except ValueError:
        return str(respuesta_usuario).strip().lower() == str(respuesta_correcta).strip().lower()

# --- INTERFAZ PRINCIPAL ---
st.title("🕵️‍♂️ CTF: Extracción de Datos")
st.write("Demuestra tu lógica en Python. Resuelve el problema en tu editor local e ingresa la respuesta exacta.")

# Barra de progreso basada en el índice (0 a 10)
progreso = st.session_state.indice_actual / 10
st.progress(progreso)
st.markdown("---")

# --- MOTOR DE PREGUNTAS ---
if st.session_state.indice_actual < 10:
    pregunta_actual = st.session_state.preguntas_estudiante[st.session_state.indice_actual]
    
    st.subheader(f"Reto {st.session_state.indice_actual + 1} de 10: {pregunta_actual['titulo']}")
    
    # Mostrar el contexto (el código/datos)
    st.info("📦 **Datos iniciales (Cópialo a tu script):**")
    st.markdown(pregunta_actual['contexto'])
    
    # Mostrar la misión
    st.warning(f"🎯 **Tu Misión:** {pregunta_actual['mision']}")
    
    respuesta = st.text_input("Ingresa el resultado de tu script aquí:")
    
    if st.button("Ejecutar Validación", type="primary"):
        if verificar_respuesta(respuesta, pregunta_actual['respuesta']):
            st.success("¡Código válido! Hash aceptado.")
            st.session_state.indice_actual += 1
            st.rerun()
        else:
            st.error("Error lógico en tu script. El resultado no coincide con el hash esperado. ¡Revisa tu código y vuelve a intentar!")

# --- PANTALLA FINAL Y CERTIFICADO ---
else:
    st.header("🏆 ¡Sistema Vulnerado Exitosamente!")
    st.success("Has completado los 10 retos aleatorios de procesamiento de datos.")
    st.balloons()
    
    st.write("Genera tu token de aprobación para el instructor:")
    nombre_estudiante = st.text_input("Ingresa tu nombre completo:")
    
    if nombre_estudiante:
        texto_certificado = f"""
        ====================================================
        TOKEN DE CERTIFICACIÓN CTF - PYTHON DATA PROCESSING
        ====================================================
        Estudiante: {nombre_estudiante}
        Retos Completados: 10 / 10
        Nivel Lógico: AVANZADO
        Validación del Servidor: APROBADO (5.0)
        ====================================================
        """
        
        st.download_button(
            label="📄 Descargar Certificado de Aprobación",
            data=texto_certificado,
            file_name=f"Certificado_CTF_{nombre_estudiante.replace(' ', '_')}.txt",
            mime="text/plain",
            type="primary"
        )
    
    st.markdown("---")
    if st.button("Reiniciar Simulador (Generará nuevas preguntas)"):
        del st.session_state.preguntas_estudiante
        st.rerun()