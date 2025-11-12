# 🌿 Plant Disease Diagnosis App (EfficientNetB0)

A deep learning web application to identify **38 different plant diseases** from leaf images.  
This model achieved **97.6% accuracy** and is deployed for free, public use on **Streamlit Cloud**.

🔗 **Live App:** [Plant Disease Diagnosis App](https://plant-disease-app-8oddx69qgn4phnrlyjp34i.streamlit.app/)

---

<img width="1440" height="790" alt="image" src="https://github.com/user-attachments/assets/92a598fd-207d-4613-ae16-d8d0c551e199" />

---

## 📖 Overview

Plant diseases are a major threat to global food security, causing massive crop losses annually.  
Traditional diagnosis methods are often slow, expensive, and inaccessible to most farmers.

This project provides a **fast, free, and highly accurate solution** — a web app where a user can upload a photo of a plant leaf and get an instant diagnosis from a powerful deep learning model.

---

## ✨ Features

- **Instant Diagnosis:** Get predictions in seconds.  
- **High Accuracy:** Achieved *97.6% validation accuracy* on 17,572 unseen images.  
- **38 Classes:** Identifies 38 different plant diseases and healthy states from the *New Plant Diseases Dataset*.  
- **Confidence Score:** Displays model confidence in each prediction.  
- **Free & Accessible:** Deployed on *Streamlit Cloud* — 100% free and usable from any phone or computer.  

---

## 🛠️ How It Works

This project is an **end-to-end machine learning pipeline**, from training to deployment.

### ⚙️ Model
- **Architecture:** EfficientNetB0 (using Transfer Learning)  
- **Reason for Choice:** Excellent balance between accuracy and computational efficiency  

### 🧠 Framework
- **TensorFlow & Keras**

### 📈 Training
- Trained in *Google Colab* on the *New Plant Diseases Dataset*  
- Dataset size: **70,295 training images** and **17,572 validation images**

### 🚀 Deployment
- The app is a single **Streamlit Python script (`app.py`)**  
- Hosted on **Streamlit Cloud**  
- The trained model (`.h5`) is downloaded automatically from a public Google Drive link  

---

## 📊 Model Performance

The final model is **highly accurate and robust**.

### ✅ Final Metrics

Performance on the 17,572-image validation set:

<img width="233" height="222" alt="metrics" src="https://github.com/user-attachments/assets/e66ccec9-a1e5-4015-993c-3324e7934bd1" />

---

### 🔢 Confusion Matrix

A strong diagonal in the confusion matrix confirms **high accuracy** and **minimal misclassification** across all 38 classes.

<img width="1848" height="1589" alt="confusion_matrix" src="https://github.com/user-attachments/assets/fb269878-9196-4a9a-975a-a480e36f3769" />

---

### 🌱 Example Predictions

Below are sample test results showing correct identification of plant diseases:

<img width="415" height="506" alt="example1" src="https://github.com/user-attachments/assets/b26c0755-0bae-4eb1-9d0a-44730172779a" />

<img width="415" height="506" alt="example2" src="https://github.com/user-attachments/assets/503f50f1-9e97-4ca6-aec6-c756922ef7ed" />

---

## 💡 Summary

- **Architecture:** EfficientNetB0 (Transfer Learning)  
- **Dataset:** New Plant Diseases Dataset  
- **Accuracy:** 97.6% on unseen validation data  
- **Deployment:** Streamlit Cloud (Fully Interactive Web App)  

---

### 🪴 Built With
- TensorFlow · Keras · Streamlit · Google Colab  
- Open access model hosting for the community 🌍  

---

⭐ *If you found this project useful, consider giving it a star on GitHub!*
