import streamlit as st
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import os
st.write(os.listdir("."))

# Load model
#model = load_model("tomato_disease_mobilenetv2.h5")
model = load_model(
    r"C:\Users\singh\OneDrive\Desktop\tomato_disease_mobilenetv2.h5",
    compile=False
)

# Class names (same order as training)
class_names = [
    'Tomato___Bacterial_spot',
    'Tomato___Early_blight',
    'Tomato___Late_blight',
    'Tomato___Leaf_Mold',
    'Tomato___Septoria_leaf_spot',
    'Tomato___Spider_mites Two-spotted_spider_mite',
    'Tomato___Target_Spot',
    'Tomato___Tomato_mosaic_virus',
    'Tomato___Tomato_Yellow_Leaf_Curl_Virus',
    'Tomato___healthy'
]

st.title("🍅 Tomato Disease Detection App")

uploaded_file = st.file_uploader("Upload a tomato leaf image", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    img = image.load_img(uploaded_file, target_size=(224, 224))
    st.image(img, caption="Uploaded Image", use_column_width=True)

    img_array = image.img_to_array(img)
    img_array = img_array / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    prediction = model.predict(img_array)
    pred_index = np.argmax(prediction)
    confidence = np.max(prediction) * 100

    st.subheader("Prediction Result")
    st.write("Disease:", class_names[pred_index])
    st.write("Confidence:", f"{confidence:.2f}%")
