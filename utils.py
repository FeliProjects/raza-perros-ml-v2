import os
import json
import gc  # <-- NUEVO: Para limpiar la memoria RAM
import numpy as np
from PIL import Image
import streamlit as st

# Importar solo lo necesario para ahorrar memoria
from tensorflow import keras
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input as _mobilenet
from tensorflow.keras.applications.resnet50 import preprocess_input as _resnet
from tensorflow.keras.applications.efficientnet import preprocess_input as _efficientnet
from tensorflow.keras.applications.vgg16 import preprocess_input as _vgg16

MODEL_PATH = os.getenv("KERAS_MODEL_PATH", "modelo_razas_perros.keras")
CLASSES_PATH = os.getenv("DOG_CLASSES_PATH", "class_names.json")
IMAGE_SIZE = (224, 224)
BASE_MODEL = os.getenv("BASE_MODEL", "mobilenet")

PREPROCESSORS = {
    "mobilenet": _mobilenet,
    "resnet": _resnet,
    "efficientnet": _efficientnet,
    "vgg16": _vgg16,
}

def clean_breed_name(breed_string):
    if isinstance(breed_string, str) and "-" in breed_string:
        return breed_string.split("-")[-1].replace("_", " ").title()
    return breed_string.replace("_", " ").title()

# NUEVO: max_entries=1 asegura que Streamlit no guarde múltiples copias pesadas en RAM
@st.cache_resource(show_spinner=False, max_entries=1)
def load_model_and_classes():
    model = keras.models.load_model(MODEL_PATH)
    with open(CLASSES_PATH, "r") as f:
        class_names = json.load(f)
    return model, class_names

def preprocess_image(image: Image.Image) -> np.ndarray:
    if image.mode != "RGB":
        image = image.convert("RGB")
    image = image.resize(IMAGE_SIZE)
    img_array = np.array(image, dtype="float32")
    preprocess_fn = PREPROCESSORS.get(BASE_MODEL, lambda x: x / 255.0)
    img_array = preprocess_fn(img_array)
    return np.expand_dims(img_array, axis=0)

def predict(image_array, model, class_names):
    # NUEVO: Cambiamos model.predict() por model(..., training=False)
    # Esto evita fugas de memoria en TensorFlow al hacer inferencias individuales
    preds = model(image_array, training=False).numpy()[0]
    
    top_indices = np.argsort(preds)[::-1][:3]
    results = []
    for idx in top_indices:
        breed = clean_breed_name(class_names[idx] if isinstance(class_names, list) else str(idx))
        results.append({"breed": breed, "probability": float(preds[idx])})
        
    # NUEVO: Limpiamos las variables pesadas y forzamos al sistema a vaciar la RAM
    del image_array
    del preds
    gc.collect()
    
    return results
