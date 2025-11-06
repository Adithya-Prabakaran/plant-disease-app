import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image
import os
import gdown  # Make sure 'gdown' is in your requirements.txt

# --- Configuration ---
st.set_page_config(page_title="Plant Disease Diagnosis", layout="centered")

# --- Google Drive File ID ---
GOOGLE_DRIVE_FILE_ID = "1QB8rvNBLAczVcZJMbrr_jaVQ_Jqfpkr0"
MODEL_FILE_PATH = "plant_disease_model_efficientnetB0.h5"

# --- Class Names ---
# Define the 38 class names in the correct order
class_names = [
    'Apple___Apple_scab', 'Apple___Black_rot', 'Apple___Cedar_apple_rust', 
    'Apple___healthy', 'Blueberry___healthy', 'Cherry_(including_sour)___Powdery_mildew',
    'Cherry_(including_sour)___healthy', 'Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot',
    'Corn_(maize)___Common_rust_', 'Corn_(maize)___Northern_Leaf_Blight', 'Corn_(maize)___healthy',
    'Grape___Black_rot', 'Grape___Esca_(Black_Measles)', 'Grape___Leaf_blight_(Isariopsis_Leaf_Spot)',
    'Grape___healthy', 'Orange___Haunglongbing_(Citrus_greening)', 'Peach___Bacterial_spot',
    'Peach___healthy', 'Pepper,_bell___Bacterial_spot', 'Pepper,_bell___healthy',
    'Potato___Early_blight', 'Potato___Late_blight', 'Potato___healthy',
    'Raspberry___healthy', 'Soybean___healthy', 'Squash___Powdery_mildew',
    'Strawberry___Leaf_scorch', 'Strawberry___healthy', 'Tomato___Bacterial_spot',
    'Tomato___Early_blight', 'Tomato___Late_blight', 'Tomato___Leaf_Mold',
    'Tomato___Septoria_leaf_spot', 'Tomato___Spider_mites Two-spotted_spider_mite',
    'Tomato___Target_Spot', 'Tomato___Tomato_Yellow_Leaf_Curl_Virus', 'Tomato___Tomato_mosaic_virus',
    'Tomato___healthy'
]

# --- Model Loading ---
# Using st.cache_resource to load the model only once
@st.cache_resource
def load_my_model():
    # Check if model file already exists
    if not os.path.exists(MODEL_FILE_PATH):
        st.write("Model file not found. Downloading from Google Drive...")
        # Download from Google Drive
        try:
            download_url = f'https://drive.google.com/uc?id={GOOGLE_DRIVE_FILE_ID}'
            gdown.download(download_url, MODEL_FILE_PATH, quiet=False)
            st.write("Model downloaded successfully.")
        except Exception as e:
            st.error(f"Error downloading model: {e}")
            return None
    
    # Load the model
    try:
        model = tf.keras.models.load_model(MODEL_FILE_PATH)
        return model
    except Exception as e:
        st.error(f"Error loading Keras model: {e}")
        return None

# --- Preprocessing Function ---
def preprocess_image(img_file):
    try:
        # Open the image file from the uploader
        img = Image.open(img_file)
        
        # Convert the image to 3 channels (RGB)
        # This handles both 4-channel RGBA and 1-channel Grayscale
        img = img.convert('RGB')        
        # Now, resize
        img = img.resize((224, 224))
        
        # Convert to NumPy array
        img_array = np.array(img)
        
        # Create a batch of 1
        img_batch = np.expand_dims(img_array, axis=0)
        return img_batch
    except Exception as e:
        st.error(f"Error preprocessing image: {e}")
        return None

# --- Streamlit User Interface ---

st.title("Plant Disease Diagnosis 🌿")
st.write("Upload an image of a plant leaf and the AI will identify the disease.")

# File uploader widget
uploaded_file = st.file_uploader("Choose a leaf image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # 1. Display the uploaded image
    st.image(uploaded_file, caption="Uploaded Image.", use_column_width=True)
    
    # 2. Add a "Classify" button
    if st.button("Diagnose"):
        # 3. Show a spinner while processing
        with st.spinner("Analyzing..."):
            
            # Preprocess the image
            image_batch = preprocess_image(uploaded_file)
            
            if image_batch is not None:
                # Load the model
                model = load_my_model()
                
                if model is not None:
                    # 4. Get prediction
                    predictions = model.predict(image_batch)
                    predicted_index = np.argmax(predictions[0])
                    predicted_class = class_names[predicted_index]
                    confidence = float(np.max(predictions[0])) * 100
                    
                    # 5. Display the result
                    st.success(f"**Diagnosis: {predicted_class}**")
                    st.info(f"**Confidence:** {confidence:.2f}%")
