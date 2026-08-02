# app.py
import streamlit as st
from PIL import Image
import time

# Importaciones locales
from styles import CUSTOM_CSS
from ui import render_sidebar, render_predictions_html
from utils import load_model_and_classes, preprocess_image, predict

def main():
    # 1. Configuración de página y CSS
    st.set_page_config(page_title="Dog Breed AI", page_icon="🐕", layout="wide")
    st.markdown(CUSTOM_CSS, unsafe_allow_html=True)
    
    # 2. Renderizar Sidebar
    render_sidebar()

    # 3. Textos principales
    st.markdown("<h1 class='main-title'>🐕 Identificador de Razas con IA</h1>", unsafe_allow_html=True)
    st.write("Sube una fotografía de un perro y la red neuronal deducirá su raza al instante.")

    # 4. Cargar modelo
    try:
        model, class_names = load_model_and_classes()
    except Exception as e:
        st.error(f"Error cargando el modelo: {e}")
        return

    # 5. Interfaz de Columnas
    col_izq, col_der = st.columns([1, 1.2], gap="large")

    with col_izq:
        uploaded_file = st.file_uploader("Sube una foto", type=["jpg", "png", "jpeg"])
        if uploaded_file:
            image = Image.open(uploaded_file)
            st.image(image, use_column_width=True)

    with col_der:
        if uploaded_file:
            st.markdown("### 📊 Análisis de la Red Neuronal")
            with st.spinner("Procesando..."):
                time.sleep(0.5)
                # Pipeline de ML
                processed_img = preprocess_image(image)
                results = predict(processed_img, model, class_names)
                
                # Renderizar resultados
                st.markdown(render_predictions_html(results), unsafe_allow_html=True)
        else:
            st.info("👈 Esperando imagen...")

if __name__ == "__main__":
    main()
