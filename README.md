# OCR Text Extraction App

A Python-based Optical Character Recognition (OCR) application that extracts text from images using the EasyOCR deep learning library. The project includes both a desktop OCR script and a user-friendly Streamlit web application for uploading images and downloading extracted text.

---

## Features

- Extract text from images using EasyOCR
- Supports multiple image formats:
  - PNG
  - JPG
  - JPEG
  - WEBP
- Displays uploaded image
- Extracts text with high accuracy
- Download extracted text as a `.txt` file
- Simple and interactive Streamlit interface
- Draws bounding boxes around detected text (OCR visualization)

---

## Technologies Used

- Python
- EasyOCR
- OpenCV
- Streamlit
- Pillow (PIL)
- NumPy
- Matplotlib

---

## Project Structure

```
OCR-Text-Extraction/
│
├── images/
│   └── sample.webp
│
├── main.py
├── ocr_test.py
├── streamlit_app.py
├── requirements.txt
├── .gitignore
└── README.md
```

---

## Installation

### Clone the repository

```bash
git clone https://github.com/Visuvanathan-K/OCR-Text-Extraction.git
```

```bash
cd OCR-Text-Extraction
```

---

### Create a virtual environment

```bash
python -m venv venv
```

Activate it:

**Windows**

```bash
venv\Scripts\activate
```

**Linux/macOS**

```bash
source venv/bin/activate
```

---

### Install dependencies

```bash
pip install -r requirements.txt
```

---

## Running the OCR Script

```bash
python ocr_test.py
```

The script will:

- Load an image
- Detect text
- Draw bounding boxes
- Display the output image

---

## Running the Streamlit App

```bash
streamlit run streamlit_app.py
```

Open the browser at:

```
http://localhost:8501
```

---

## How It Works

1. Upload an image.
2. EasyOCR detects text regions.
3. Text is recognized using a deep learning model.
4. Extracted text is displayed.
5. Users can download the extracted text as a `.txt` file.

---

## Supported Image Formats

- PNG
- JPG
- JPEG
- WEBP

---

## Future Improvements

- Multi-language OCR support
- PDF text extraction
- Handwritten text recognition
- Batch image processing
- Export results to PDF or Word
- OCR confidence visualization

---

## Screenshots

Add screenshots of your application here.

Example:

```
screenshots/
    home.png
    result.png
```

Then include:

```markdown
![Home](screenshots/home.png)

![Result](screenshots/result.png)
```

---

## Author

**Visuvanathan K**

GitHub:
https://github.com/Visuvanathan-K

---

## License

This project is licensed under the MIT License.
