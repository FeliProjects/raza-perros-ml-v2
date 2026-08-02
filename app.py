# app.py
import streamlit as st
from PIL import Image
import time

# Importaciones locales
from styles import CUSTOM_CSS
from ui import render_sidebar, render_predictions_html
from utils import load_model_and_classes, preprocess_image, predict

def main():
    st.set_page_config(page_title="Dog Breed AI", page_icon="🐕", layout="wide")
    st.markdown(CUSTOM_CSS, unsafe_allow_html=True)
    
    render_sidebar()

    st.markdown("<h1 style='text-align: center; color: #1f2937;'>🐕 Identificador de Razas con IA</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #6b7280; font-size: 1.1rem;'>Sube una fotografía de un perro y la red neuronal deducirá su raza al instante.</p>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)

    try:
        model, class_names = load_model_and_classes()
    except Exception as e:
        st.error(f"Error cargando el modelo: {e}")
        return

    # ---------------------------------------------------------
    # MANEJO DE ESTADO PARA EJEMPLOS
    # ---------------------------------------------------------
    if "ejemplo_actual" not in st.session_state:
        st.session_state.ejemplo_actual = None

    col_izq, col_der = st.columns([1, 1.2], gap="large")

    with col_izq:
        st.markdown("### 📸 Sube una foto")
        uploaded_file = st.file_uploader("", type=["jpg", "png", "jpeg", "webp"], label_visibility="collapsed")
        
        # Lógica de qué imagen usar
        if uploaded_file:
            # Si el usuario sube algo manualmente, limpiamos la memoria del ejemplo
            st.session_state.ejemplo_actual = None
            image = Image.open(uploaded_file)
        elif st.session_state.ejemplo_actual:
            # Si no hay archivo subido pero se hizo clic en un ejemplo
            image = Image.open(st.session_state.ejemplo_actual)
        else:
            image = None
            
        # Botones de ejemplo (Solo se muestran si no se ha subido una foto manualmente)
        if not uploaded_file:
            st.markdown("<p style='color: #4b5563; margin-top: 10px;'>💡 <b>¿No tienes una foto?</b> Prueba con estas:</p>", unsafe_allow_html=True)
            col_btn1, col_btn2 = st.columns(2)
            
            # REEMPLAZA LOS NOMBRES EXACTOS DE TUS ARCHIVOS AQUÍ:
            if col_btn1.button("🐶 Probar Ejemplo 1", use_column_width=True):
                st.session_state.ejemplo_actual = "assets/ejemplo1_husky.jpeg" # <-- Nombre de tu imagen 1
                st.rerun()
            if col_btn2.button("🦴 Probar Ejemplo 2", use_column_width=True):
                st.session_state.ejemplo_actual = "assets/ejemplo2_pug.jpeg" # <-- Nombre de tu imagen 2
                st.rerun()

        # Mostrar la imagen seleccionada (ya sea subida o ejemplo)
        if image is not None:
            st.image(image, use_container_width=True)

    with col_der:
        if image is not None:
            st.markdown("### 📊 Análisis de la Red Neuronal")
            with st.spinner("Procesando la anatomía del perro..."):
                time.sleep(0.5) # Pequeña pausa intencional para UX
                processed_img = preprocess_image(image)
                results = predict(processed_img, model, class_names)
                
                # Renderizar resultados
                st.markdown(render_predictions_html(results), unsafe_allow_html=True)
        else:
             st.markdown(
                "<div style='border: 2px dashed #d1d5db; border-radius: 12px; height: 300px; display: flex; align-items: center; justify-content: center; color: #9ca3af;'>"
                "Sube una imagen o selecciona un ejemplo para comenzar...</div>", 
                unsafe_allow_html=True
            )

if __name__ == "__main__":
    main()
