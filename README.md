# 🌿 AI Crop Disease Detection

An AI-powered web application that detects tomato leaf diseases from uploaded images using a Convolutional Neural Network (CNN) built with TensorFlow and deployed using Streamlit.

## 🚀 Live Demo

🔗 https://ai-crop-disease-detection-smnjgaxuxpvwmdgwxxne2k.streamlit.app/

## 📂 GitHub Repository

🔗 https://github.com/akhilajp2004/AI-Crop-Disease-Detection

---

## 📖 Project Overview

This application allows users to upload an image of a tomato leaf and automatically predicts whether the leaf is healthy or affected by one of the supported diseases. The application also provides the prediction confidence and recommended treatment.

---

## ✨ Features

- Upload tomato leaf images
- AI-based disease prediction using CNN
- Prediction confidence score
- Disease-specific treatment recommendations
- User-friendly Streamlit interface
- Deployed online for easy access

---

## 🦠 Supported Classes

- 🟢 Healthy Tomato Leaf
- 🍂 Tomato Early Blight
- 🍂 Tomato Late Blight
- 🍂 Tomato Leaf Mold
- 🍂 Tomato Septoria Leaf Spot

---

## 🛠️ Technologies Used

- Python
- TensorFlow / Keras
- Streamlit
- NumPy
- Pillow
- Matplotlib
- Scikit-learn

---

## 🧠 Deep Learning Model

- Model: Convolutional Neural Network (CNN)
- Framework: TensorFlow / Keras
- Input Image Size: 128 × 128
- Activation Function: ReLU
- Output Layer: Softmax
- Optimizer: Adam
- Loss Function: Categorical Crossentropy

---

## 📊 Dataset

The model was trained using a subset of the PlantVillage tomato leaf dataset containing five classes.

Classes:

- Tomato Healthy
- Tomato Early Blight
- Tomato Late Blight
- Tomato Leaf Mold
- Tomato Septoria Leaf Spot

The dataset is used only for model training and is not included in this repository because of its large size. Public plant disease datasets such as PlantVillage are commonly used for this type of image classification research. :contentReference[oaicite:0]{index=0}

---

## 📷 Application Workflow

1. Upload a tomato leaf image.
2. Image preprocessing.
3. CNN predicts the disease.
4. Display:
   - Disease Name
   - Confidence Score
   - Recommended Treatment

---

## 📁 Project Structure

```
AI-Crop-Disease-Detection/
│
├── models/
│   └── crop_model.keras
│
├── uploads/
│
├── app.py
├── predict.py
├── model.py
├── treatment.py
├── train_model.py
├── requirements.txt
├── runtime.txt
└── README.md
```

---

## ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/akhilajp2004/AI-Crop-Disease-Detection.git
```

Move into the project

```bash
cd AI-Crop-Disease-Detection
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
streamlit run app.py
```

---

## 🎯 Future Improvements

- Support additional crops
- Detect more diseases
- Mobile application
- Real-time camera detection
- Cloud database integration
- Higher accuracy using transfer learning

---

## 👩‍💻 Developer

**Akhila J Puttanani**

Computer Science and Engineering Student

---

## 📄 License

This project is developed for educational and academic purposes.