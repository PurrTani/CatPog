# -*- coding: utf-8 -*-
"""catpog.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1xkEAwPHwvjeoS7JD7LXCnk-grbDa-jrh
"""

import streamlit as st
from PIL import Image
import os

upload_dir = "images"

if not os.path.exists(upload_dir):
  os.makedirs(upload_dir)

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
  filename = uploaded_file.name
  save_path = os.path.join(upload_dir, filename)

with open(save_path, "wb") as f:
  f.write(uploaded_file.getbuffer())

image = Image.open(save_path)

st.title('Cat Pog')

st.image(image, caption='You tellin me a shrimp fried this rice?')
