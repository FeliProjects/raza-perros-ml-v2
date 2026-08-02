# utils.py
import os
import json
import numpy as np
from PIL import Image
import streamlit as st
from tensorflow import keras
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input

# Variables de entorno o constantes
MODEL_PATH = "modelo_razas_perros.keras"
CLASSES_PATH = "class_names.json"
IMAGE_SIZE = (224, 224)

@st.cache_resource(show_spinner=False)
def load_model_and_classes():
    model = keras.models.load_model(MODEL_PATH)
    with open(CLASSES_PATH, "r") as f:
        class_names = json.load(f)
    return model, class_names

def preprocess_image(image: Image.Image) -> np.ndarray:
    # Lógica de conversión a RGB, resize y preprocess_input...
    pass

def predict(image_array, model, class_names):
    # Lógica de model.predict, argsort y limpieza de string...
    pass