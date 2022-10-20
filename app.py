import streamlit as st
from img_classification import teachable_machine_classification
import keras
from PIL import Image, ImageOps
import numpy as np

st.title("Aplicación de reconocimiento de celúlas sanguíneas")

st.balloons()

uploaded_file = st.file_uploader("Carga una imagen ...", type=["jpg","jpeg"])
if uploaded_file is not None:
  image = Image.open(uploaded_file)
  st.sidebar.image(image)
  label = teachable_machine_classification(image, 'keras_model.h5')
  st.write("jaja",label)
  if label == 0:
    st.write("EOSINOFILO")
  elif label == 1:
    st.write("LINFOCITO")
  else:
    st.write("MONOCITO")
