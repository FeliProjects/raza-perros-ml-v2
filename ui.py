import streamlit as st

def render_sidebar():
    with st.sidebar:
        st.image("https://cdn-icons-png.flaticon.com/512/616/616408.png", width=80) 
        st.title("Sobre el Proyecto")
        st.write("""
        Este proyecto forma parte de mi portafolio de Machine Learning. 
        Utiliza **Transfer Learning** para identificar razas de perros con alta precisión.
        """)
        st.markdown("### 🛠️ Detalles Técnicos")
        st.markdown("- **Arquitectura Base:** `MobileNet`")
        st.markdown("- **Tamaño del Modelo:** ~12 MB")
        st.markdown("- **Input:** `224x224 RGB`")
        
        st.divider()
        st.markdown("### 👨‍💻 Desarrollador")
        st.markdown("[🔗 Mi LinkedIn](#)")
        st.markdown("[🐈 Mi GitHub](#)")

def render_predictions_html(predictions):
    """Devuelve el string HTML con las medallas y barras de progreso completas."""
    html = '<div style="margin-top: 1rem;">'
    for i, pred in enumerate(predictions):
        pct = pred["probability"] * 100
        rank_emoji = ["🥇", "🥈", "🥉"][i]
        fill_class = ["gold-fill", "silver-fill", "bronze-fill"][i]
        
        badge = '<span class="confidence-badge">Alta Confianza ✓</span>' if i == 0 and pct > 70 else ''
        
        html += f"""
        <div class="prediction-card">
            <div class="rank-icon">{rank_emoji}</div>
            <div class="details-container">
                <div class="breed-title">{pred['breed']} {badge}</div>
                <div class="progress-bg">
                    <div class="progress-fill {fill_class}" style="width: {pct}%;"></div>
                </div>
            </div>
            <div class="percentage">{pct:.1f}%</div>
        </div>
        """
    html += '</div>'
    return html
