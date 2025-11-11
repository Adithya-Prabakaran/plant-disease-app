# 🌿 Plant Disease Diagnosis App (EfficientNetB0)

A deep learning web application to identify 38 different plant diseases from leaf images. This model achieved 97.6% accuracy and is deployed for free, public use on Streamlit Cloud.

https://plant-disease-app-8oddx69qgn4phnrlyjp34i.streamlit.app/


<img width="1440" height="790" alt="image" src="https://github.com/user-attachments/assets/92a598fd-207d-4613-ae16-d8d0c551e199" />



📖 Overview
Plant diseases are a major threat to global food security, causing massive crop losses annually . Traditional diagnosis methods are often slow, expensive, and inaccessible to most farmers .


This project provides a fast, free, and highly accurate solution. It's a web app where a user can upload a photo of a plant leaf and get an instant diagnosis from a powerful deep learning model.

✨ Features
Instant Diagnosis: Get a prediction in seconds.


High Accuracy: The model achieved 97.6% validation accuracy on 17,572 unseen images.


38 Classes: Can identify 38 different plant diseases and healthy states from the "New Plant Diseases Dataset".


Confidence Score: Shows the model's confidence in its prediction.


Free & Accessible: Deployed on Streamlit Cloud, it's 100% free and accessible from any phone or computer with a web browser.


🛠️ How It Works: Tech Stack & Model

This project is an end-to-end machine learning pipeline, from training to deployment.


Model: EfficientNetB0 (using Transfer Learning). This model was chosen for its excellent balance of high accuracy and computational efficiency.



Framework: TensorFlow & Keras.


Training: The model was trained in Google Colab on the "New Plant Diseases Dataset" (70,295 training images, 17,572 validation images).


Deployment: The app is a single Streamlit Python script (app.py). It's hosted for free on Streamlit Cloud and automatically downloads the trained model file (.h5) from a public Google Drive link .


📊 Model Performance
The final model is highly accurate and robust.

Final Metrics
The model's performance on the 17,572-image validation set:


<img width="233" height="222" alt="image" src="https://github.com/user-attachments/assets/e66ccec9-a1e5-4015-993c-3324e7934bd1" />

Confusion Matrix
The confusion matrix for all 38 classes shows a very strong diagonal, confirming high accuracy and minimal confusion between classes.


<img width="1848" height="1589" alt="confusion_matrix" src="https://github.com/user-attachments/assets/fb269878-9196-4a9a-975a-a480e36f3769" />


Example Predictions
The model correctly identifies various diseases from the test set.


<img width="415" height="506" alt="image" src="https://github.com/user-attachments/assets/b26c0755-0bae-4eb1-9d0a-44730172779a" />

<img width="415" height="506" alt="image" src="https://github.com/user-attachments/assets/503f50f1-9e97-4ca6-aec6-c756922ef7ed" />

