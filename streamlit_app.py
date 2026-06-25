import streamlit as st
import easyocr
from PIL import Image
import numpy as np

st.title("OCR Text Extraction App")

uploaded_file = st.file_uploader(
    "Upload an image",
    type=["png", "jpg", "jpeg", "webp"]
)

if uploaded_file is not None:

    image = Image.open(uploaded_file)

    st.image(image, caption="Uploaded Image", use_container_width=True)

    with st.spinner("Extracting text..."):

        reader = easyocr.Reader(['en'])

        results = reader.readtext(np.array(image))

        extracted_text = ""

        for result in results:
            extracted_text += result[1] + "\n"

    st.subheader("Extracted Text")

    st.text_area(
        "OCR Output",
        extracted_text,
        height=200
    )

    st.download_button(
        "Download Text",
        extracted_text,
        file_name="ocr_output.txt"
    )