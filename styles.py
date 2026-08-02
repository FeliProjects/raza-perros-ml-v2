# styles.py
CUSTOM_CSS = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}

.prediction-card {
    display: flex;
    align-items: center;
    background: white;
    border-radius: 12px;
    padding: 1.2rem;
    margin-bottom: 1rem;
    box-shadow: 0 4px 6px rgba(0,0,0,0.05);
    border: 1px solid #f0f2f6;
    transition: transform 0.2s ease, box-shadow 0.2s ease;
}
.prediction-card:hover {
    transform: translateY(-2px);
    box-shadow: 0 8px 15px rgba(0,0,0,0.1);
}
.rank-icon {
    font-size: 2rem;
    margin-right: 1.5rem;
    min-width: 40px;
    text-align: center;
}
.details-container {
    flex-grow: 1;
}
.breed-title {
    font-size: 1.15rem;
    font-weight: 700;
    color: #1f2937;
    margin-bottom: 0.3rem;
    text-transform: capitalize;
}
.confidence-badge {
    background-color: #dcfce7;
    color: #166534;
    padding: 0.2rem 0.6rem;
    border-radius: 9999px;
    font-size: 0.75rem;
    font-weight: 600;
    margin-left: 0.5rem;
}
.progress-bg {
    width: 100%;
    background-color: #e5e7eb;
    border-radius: 9999px;
    height: 10px;
    margin-top: 0.5rem;
    overflow: hidden;
}
.progress-fill {
    height: 100%;
    border-radius: 9999px;
    transition: width 1s ease-in-out;
}
.gold-fill { background: linear-gradient(90deg, #F59E0B, #FBBF24); }
.silver-fill { background: linear-gradient(90deg, #9CA3AF, #D1D5DB); }
.bronze-fill { background: linear-gradient(90deg, #B45309, #D97706); }

.percentage {
    font-weight: 700;
    color: #4b5563;
    font-size: 1.1rem;
    margin-left: 1rem;
    min-width: 60px;
    text-align: right;
}
/* --- TRADUCCIÓN DEL FILE UPLOADER --- */
[data-testid="stFileUploadDropzone"] div div::before {
    content: "📁 Arrastra y suelta la foto de un perro aquí";
    color: #1f2937;
    font-weight: 600;
    font-size: 1.1rem;
    display: block;
    margin-bottom: 5px;
}
[data-testid="stFileUploadDropzone"] div div::after {
    content: "Límite: 10MB por archivo • JPG, PNG, WEBP";
    color: #6b7280;
    font-size: 0.85rem;
    display: block;
    margin-top: 5px;
}
[data-testid="stFileUploadDropzone"] div div span {
    display: none; /* Oculta el texto "Drag and drop file here" */
}
[data-testid="stFileUploadDropzone"] div div small {
    display: none; /* Oculta el límite original en inglés */
}
/* Forzar que el texto del botón siga visible */
button[data-testid="baseButton-secondary"] span {
    display: block !important;
}
</style>
"""
