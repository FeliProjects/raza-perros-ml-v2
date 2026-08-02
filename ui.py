# ui.py
import streamlit as st

def render_sidebar():
    with st.sidebar:
        st.image("icono.png", width=80)
        st.title("Sobre el Proyecto")
        # Textos del sidebar...

def render_predictions_html(predictions):
    """Devuelve el string HTML con las medallas y barras de progreso"""
    html = '<div style="margin-top: 1rem;">'
    # Bucle for para armar las tarjetas...
    html += '</div>'
    return html