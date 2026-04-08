import streamlit as st
import math

# --- CONFIGURACIÓN DE LA PÁGINA ---
st.set_page_config(page_title="Escape Room Python", page_icon="🐍", layout="centered")

# --- INICIALIZACIÓN DEL ESTADO ---
# Esto permite que la aplicación "recuerde" en qué nivel va el estudiante
if 'nivel' not in st.session_state:
    st.session_state.nivel = 1

# --- FUNCIÓN DE VALIDACIÓN ---
def verificar_respuesta(respuesta_usuario, respuesta_correcta):
    """Compara la respuesta tolerando decimales o strings"""
    if respuesta_usuario == "":
        return False
    try:
        # Intenta comparar como números flotantes (para tolerar 169 vs 169.0)
        val_usuario = float(respuesta_usuario.strip())
        val_correcta = float(respuesta_correcta)
        return math.isclose(val_usuario, val_correcta, rel_tol=1e-4)
    except ValueError:
        # Si falla, compara como texto exacto (sin espacios)
        return str(respuesta_usuario).strip().lower() == str(respuesta_correcta).strip().lower()

# --- INTERFAZ PRINCIPAL ---
st.title("🕵️‍♂️ La Búsqueda del Dataset Perdido")
st.write("Abre tu editor de Python (Colab, VS Code o IDLE). Resuelve el problema de cada sala usando código y digita aquí el resultado para avanzar.")
st.progress(st.session_state.nivel / 5) # Barra de progreso visual
st.markdown("---")

# --- NIVEL 1 ---
if st.session_state.nivel == 1:
    st.header("Sala 1: La Bóveda de Strings")
    st.info("""
    Has encontrado un registro de datos corrupto en formato string:
    `log = "id_94_val_7.5"`
    
    **Tu misión:** 1. Usa métodos de string para dividir la cadena.
    2. Extrae el ID y conviértelo a entero (`int`).
    3. Extrae el valor y conviértelo a decimal (`float`).
    4. Multiplica el valor por 10 y súmalo al ID. 
    
    ¿Cuál es el número de acceso resultante?
    """)
    
    respuesta = st.text_input("Ingresa la clave de acceso:")
    if st.button("Verificar Código", type="primary"):
        if verificar_respuesta(respuesta, 169):
            st.success("¡Acceso concedido! Avanzando a la Sala 2...")
            st.session_state.nivel = 2
            st.rerun()
        else:
            st.error("Acceso denegado. Revisa tu lógica, el 'casting' de variables y vuelve a intentar.")

# --- NIVEL 2 ---
elif st.session_state.nivel == 2:
    st.header("Sala 2: El Filtro de Ruido")
    st.info("""
    El acceso te dio un dataset sucio. Cópialo en tu editor:
    `datos = [10, -5, 20, 999, 15, 0, -20]`
    
    **Tu misión:** Debes limpiarlo usando un ciclo `for` y condicionales `if`. 
    1. Descarta los números negativos (menores a 0).
    2. Descarta el error de lectura del sensor (el número 999).
    
    ¿Cuál es la suma matemática de los datos válidos restantes?
    """)
    
    respuesta = st.text_input("Ingresa la suma de los datos válidos:")
    if st.button("Verificar Código", type="primary"):
        if verificar_respuesta(respuesta, 45):
            st.success("¡Filtro exitoso! Avanzando a la Sala 3...")
            st.session_state.nivel = 3
            st.rerun()
        else:
            st.error("La suma es incorrecta. ¿Aseguraste filtrar tanto los negativos como el 999?")

# --- NIVEL 3 ---
elif st.session_state.nivel == 3:
    st.header("Sala 3: Navegación del Clúster")
    st.info("""
    Un algoritmo de agrupamiento inicia en las coordenadas `x = 0` y `y = 0`. 
    
    **Tu misión:**
    1. Crea un ciclo `while` que se ejecute *mientras* `x < 3`.
    2. En cada iteración del ciclo, `x` debe aumentar en 1, y `y` debe aumentar en 2.
    3. Al terminar el ciclo, usa la librería `math` (`math.sqrt`) para calcular la distancia euclidiana desde el origen `(0,0)` hasta las coordenadas finales del algoritmo.
    4. Redondea el resultado a 2 decimales usando `round(resultado, 2)`.
    
    ¿Cuál es la distancia final?
    """)
    
    respuesta = st.text_input("Ingresa la distancia calculada:")
    if st.button("Verificar Código", type="primary"):
        if verificar_respuesta(respuesta, 6.71):
            st.success("¡Navegación completada! Avanzando a la Sala 4...")
            st.session_state.nivel = 4
            st.rerun()
        else:
            st.error("Distancia incorrecta. Verifica las iteraciones del ciclo y la fórmula de distancia.")

# --- NIVEL 4 ---
elif st.session_state.nivel == 4:
    st.header("Sala 4: La Llave Maestra")
    st.info("""
    Has llegado al servidor principal. La clave está oculta en este diccionario:
    `data = {"Modelo_A": [1, 2, 3], "Modelo_B": [4, 5, 6]}`
    
    **Tu misión:**
    1. Crea una variable para sumar los resultados.
    2. Usando un ciclo `for`, recorre el diccionario.
    3. Encuentra el valor máximo (`max()`) de cada lista dentro del diccionario.
    4. Suma esos valores máximos.
    
    ¿Cuál es la llave maestra?
    """)
    
    respuesta = st.text_input("Ingresa la llave maestra:")
    if st.button("Verificar Código", type="primary"):
        if verificar_respuesta(respuesta, 9):
            st.success("¡Desbloqueo completado!")
            st.balloons() # Animación de celebración
            st.session_state.nivel = 5
            st.rerun()
        else:
            st.error("Llave incorrecta. Revisa cómo estás iterando los valores del diccionario.")

# --- PANTALLA FINAL ---
elif st.session_state.nivel == 5:
    st.header("🎉 ¡Misión Cumplida!")
    st.success("Has recuperado el dataset de Inteligencia Artificial perdido y demostrado tu dominio en Python.")
    st.write("Por favor, levanta la mano o avisa al instructor para registrar tu calificación de 5.0.")
    
    if st.button("Reiniciar Evaluación"):
        st.session_state.nivel = 1
        st.rerun()