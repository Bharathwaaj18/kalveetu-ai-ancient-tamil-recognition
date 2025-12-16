# Kalveetu AI – Ancient Tamil Script Recognition using GAN-based Data Augmentation

**93% CNN Accuracy | GAN-based Data Augmentation | Low-Data Regime Solution**

Kalveetu AI is a deep learning project that focuses on recognizing ancient Tamil-Brahmi (Thamizhi) characters from stone inscriptions and mapping them to their modern Tamil equivalents. The project addresses the extreme data scarcity problem common in historical and epigraphical datasets.

---

## 🎯 Problem Statement

* Ancient Tamil inscriptions often have **only ~1 image per character**
* Standard deep learning models fail due to **insufficient training data**
* Manual data collection or annotation is **not feasible** for historical scripts

---

## ✅ Proposed Solution (2-Stage Pipeline)

### 1️⃣ GAN-based Data Augmentation

* A Generative Adversarial Network (GAN) is trained per character
* Generates **100× synthetic images per class** from a single real sample
* Expands the dataset while preserving visual characteristics of inscriptions

### 2️⃣ CNN-based Character Classification

* A Convolutional Neural Network is trained on the augmented dataset
* Predicts **ancient Tamil-Brahmi → modern Tamil characters**
* Achieves strong performance despite the low-data regime

---

## 📊 Results

| Model          | Dataset Type               | Accuracy |
| -------------- | -------------------------- | -------- |
| CNN Classifier | GAN-Augmented Tamil-Brahmi | **93%**  |

---

## 🛠 Tech Stack

* **PyTorch**
* **GAN (Generator + Discriminator)**
* **CNN (Image Classification)**
* ImageFolder Pipeline
* Jupyter Notebook
* NumPy, Matplotlib, PIL

---

## 🚀 Quick Start

```bash
git clone https://github.com/your-username/kalveetu-ai.git
cd kalveetu-ai
pip install -r requirements.txt
jupyter notebook
```

### Notebooks

1. `gan data augmentation.ipynb` – GAN training & synthetic data generation
2. `cnn tamil recognition.ipynb` – CNN training & evaluation (93% accuracy)

---

## 📁 Repository Structure

```
kalveetu-ai/
├── gan data augmentation.ipynb   # GAN for data augmentation
├── cnn tamil recognition.ipynb   # CNN classifier (93% accuracy)
└── README.md
```

---

## 🔮 Future Work

* ✅ **Phase 1:** GAN + CNN for single-character recognition (Completed)
* ⏳ **Phase 2:** CRNN-based sequence OCR for full inscriptions
* ⏳ **Phase 3:** Streamlit web app + ONNX model deployment
* ⏳ **Phase 4:** Translation 

---

## 👤 Author

**Bharathwaaj**
Final-Year AI Engineering Student
Interests: Deep Learning • Computer Vision • Generative AI
