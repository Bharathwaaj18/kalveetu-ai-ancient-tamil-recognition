
# 📜 Kalveetu AI – Ancient Tamil Character Recognition

**Kalveetu AI** is a deep learning–based OCR web application that recognizes ancient Tamil (Thamizhi) inscription characters and maps them to their modern Tamil equivalents. The system uses a CNN model built with PyTorch and a Streamlit interface for real-time prediction.

---

 ✨ Features

- 🧠 CNN-based ancient Tamil character recognition  
- 📸 Upload character images and get instant predictions  
- 📊 Confidence score for each prediction  
- 🗂️ Prediction logging using SQLite  
- 🧩 Clean, modular, production-style Python code  
- 💻 Simple and intuitive Streamlit UI  

---

## 🏗️ Project Structure



```
kalveetu-ai/
│
├── app.py # Streamlit application
├── config.py # Configuration & UI styling
├── model.py # CNN architecture
├── model_manager.py # Model loading & prediction
├── database.py # SQLite database handling
├── utils.py # Helper functions
│
├── models/
│ └── tamil_model_weights.pth (not included)
│
├── requirements.txt
└── README.md
```
## 🧠 Model Overview

- **Input:** RGB character image (64 × 64)  
- **Model:** Convolutional Neural Network (CNN)  
- **Output:** Predicted Tamil character + confidence score  
- **Framework:** PyTorch  

---

## 🚀 How to Run the Application

1️⃣ Clone the repository:

```bash
git clone https://github.com/USERNAME/kalveetu-ai.git
cd kalveetu-ai
````

2️⃣ Create a virtual environment (recommended):

```bash
python -m venv venv
source venv/bin/activate       # Windows: venv\Scripts\activate
```

3️⃣ Install dependencies:

```bash
pip install -r requirements.txt
```

4️⃣ Download model weights:

Model weights are not included in this repository.
➡️ Download from: [Add your model link here]

Place the file in:

```
models/tamil_model_weights.pth
```

5️⃣ Run the Streamlit app:

```bash
streamlit run app.py
```

---

## 🖼️ Output

* Upload an image of an ancient Tamil character
* The predicted modern Tamil character is displayed
* Confidence score shown alongside the prediction

*(You can add screenshots here for better presentation)*

---

## 🗃️ Prediction Logging

Predictions are stored using SQLite. Logged details include:

* Image filename
* Predicted character
* Confidence score
* Timestamp

---

## 🛠️ Tech Stack

* Python
* PyTorch
* Streamlit
* SQLite
* PIL / Torchvision

---

## 📌 Notes

* Trained model weights are excluded to keep the repository lightweight
* This repository focuses on application-level deployment and inference

---

## 📜 License

This project is intended for educational and academic use.

```
