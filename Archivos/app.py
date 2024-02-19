from flask import Flask, request, render_template
from keras.models import load_model
import numpy as np
from PIL import Image
import io

app = Flask(__name__)

# Carga el modelo guardado
modelo = load_model('modelo.h5')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Obtiene el archivo de imagen de la solicitud
    file = request.files['image']
    
    # Lee el archivo de imagen
    image = Image.open(io.BytesIO(file.read()))
    
    # Preprocesa la imagen (redimensiona, normaliza, etc.)
    processed_image = preprocess_image(image)
    
    # Realiza la predicción utilizando el modelo cargado
    prediction = modelo.predict(np.array([processed_image]))
    
    # Retorna la predicción como respuesta
    return {'prediction': prediction.tolist()}

def preprocess_image(image):
    # Redimensiona la imagen según sea necesario
    resized_image = image.resize((299, 299))
    
    # Convierte la imagen a un array NumPy y normaliza
    image_array = np.array(resized_image) / 255.0
    
    return image_array
