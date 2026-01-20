# 🫀 **Deploying Heart Disease Model - Flask Web App**  

## **1. Introduction**  
Cardiovascular diseases are a leading cause of mortality worldwide, making early detection **crucial** for effective treatment and prevention. This project develops a **Flask-based web application** that predicts the likelihood of heart disease based on **key health indicators** such as **age, cholesterol levels, chest pain type, and more**. By leveraging **machine learning (Random Forest)** and **real-time model deployment**, this system provides a **fast, accessible, and user-friendly** tool for heart disease prediction.  

---

## **2. Background**  
Traditional heart disease diagnosis relies on medical tests that may not always be **immediately accessible** to patients. This project aims to:  

✅ **Provide an AI-driven, web-based risk assessment tool**.  
✅ **Enable real-time predictions** using machine learning.  
✅ **Improve accessibility** for early detection of heart disease.  
✅ **Demonstrate end-to-end ML deployment** with Flask.  

By integrating **machine learning with a web-based interface**, this project **bridges the gap between AI and healthcare**, making **predictive diagnostics more accessible**.  

---

## **3. Data Collection and Processing**  
### **📂 Dataset**  
The model is trained on a **Heart Disease Dataset**, which includes the following **features**:  

| Feature | Description |
|---------|------------|
| `age` | Age of the individual |
| `sex` | Gender (1 = Male, 0 = Female) |
| `cp` | Chest pain type (Categorical: 0-3) |
| `trestbps` | Resting blood pressure (mm Hg) |
| `chol` | Serum cholesterol (mg/dl) |
| `fbs` | Fasting blood sugar (>120 mg/dl, 1 = True, 0 = False) |
| `restecg` | Resting electrocardiographic results |
| `thalach` | Maximum heart rate achieved |
| `exang` | Exercise-induced angina (1 = Yes, 0 = No) |
| `oldpeak` | ST depression induced by exercise relative to rest |
| `slope` | Slope of the peak exercise ST segment |
| `ca` | Number of major vessels (0-3) colored by fluoroscopy |
| `thal` | Thalassemia type (0-3) |
| **Target (`output`)** | 1 = Heart Disease Present, 0 = No Heart Disease |

### **🛠️ Data Preprocessing Steps**  
✅ **Ordinal Encoding** for categorical variables.  
✅ **MinMax Scaling** for numerical features.  
✅ **Handling missing values & outliers** to ensure model accuracy.  
✅ **Feature selection & transformation** to optimize predictions.  

---

## **4. Exploratory Data Analysis (EDA)**  
📊 **Feature Correlation Analysis**  
- Identified relationships between **age, cholesterol, blood pressure, and heart disease risk**.  
- Used **heatmaps and scatter plots** to visualize key trends.  

📈 **Distribution of Patients with Heart Disease**  
- Analyzed **age and gender distribution** of affected patients.  
- Identified **high-risk factors** contributing to heart disease.  

---

## **5. Model Development**  
### **📌 Machine Learning Model Used**  
- **Random Forest Classifier** for high accuracy and robustness.  
- Trained using **Scikit-learn**, achieving a **high precision and recall**.  
- Optimized hyperparameters to improve **model generalization**.  

📊 **Model Performance:**  
✅ **Accuracy:** 90%  
✅ **Precision & Recall:** Optimized for medical diagnosis  

---

## **6. Web App Development & Deployment**  
This web app is built using **Flask**, a lightweight Python framework for **real-time predictions**.  

### 📡 **Web Application Features**  
✅ **User-friendly interface** (HTML + CSS) for health data input.  
✅ **Real-time model predictions** with instant feedback.  
✅ **Fully deployed Flask app** running locally or on the cloud.  

---

## **7. Future Work**  
+ 🔹 Integrate Deep Learning Models for enhanced accuracy.
+ 🔹 Deploy on Cloud Platforms like AWS, Heroku, or Google Cloud.
+ 🔹 Implement an API for external applications to consume predictions.
+ 🔹 Add more user-friendly visualization dashboards.

## **7. Technologies Used**  
+ 🔹 Programming: Python, HTML, CSS
+ 🔹 Machine Learning: Scikit-learn, Random Forest Classifier
+ 🔹 Web Framework: Flask
+ 🔹 Data Processing: Pandas, NumPy
+ 🔹 Model Deployment: Pickle
+ 🔹 UI Design: HTML, CSS


