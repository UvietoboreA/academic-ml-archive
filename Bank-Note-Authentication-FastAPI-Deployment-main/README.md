# 🏦 Bank Note Authentication API - FastAPI Deployment 🚀  

## **1. Introduction**  
With the rise in counterfeit banknotes, financial institutions need **robust, AI-powered authentication systems** to verify the legitimacy of currency notes. This project develops a **FastAPI-based Bank Note Authentication API** that determines whether a banknote is **genuine or fake** based on its **variance, skewness, curtosis, and entropy**. By leveraging **machine learning and real-time API deployment**, this system provides a **fast, scalable, and reliable** solution for banknote verification.  

---

## **2. Background**  
Counterfeit currency poses a major challenge for financial institutions, leading to significant losses and security risks. Traditional verification methods are often:  

- **Manual and time-consuming**, requiring human inspection.  
- **Inconsistent**, leading to potential misclassification.  
- **Lacking scalability**, making them ineffective for large-scale operations.  

This project aims to solve these challenges by:  

✅ **Automating banknote authentication** with an AI-driven model.  
✅ **Deploying a FastAPI-based RESTful service** for real-time predictions.  
✅ **Improving accuracy** using machine learning techniques.  
✅ **Providing scalable deployment options** via cloud or containerization (Docker).  

---

## **3. Data Collection and Processing**  
### **📂 Dataset**  
The dataset consists of numerical features extracted from genuine and counterfeit banknotes using **image processing techniques**. It contains the following attributes:  

| Feature | Description |
|---------|------------|
| `variance` | Variance of wavelet-transformed image |
| `skewness` | Skewness of wavelet-transformed image |
| `curtosis` | Curtosis of wavelet-transformed image |
| `entropy` | Entropy of wavelet-transformed image |

**Target:**  
- **1** → Genuine banknote  
- **0** → Fake banknote  

### **🛠️ Data Preprocessing Steps**  
✅ Normalized numerical values for model training.  
✅ Split dataset into **training (80%) and testing (20%)**.  
✅ Applied **scaling** for better model performance.  

---

## **4. Exploratory Data Analysis (EDA)**  
📊 **Feature Distribution Analysis**  
- Checked distribution of variance, skewness, curtosis, and entropy.  
- Identified patterns in data to distinguish between real and fake notes.  

📈 **Correlation Analysis**  
- Examined relationships between features to understand impact on classification.  

---

## **5. Model Development**  
### **📌 Machine Learning Model Used**  
- **Random Forest Classifier** for high accuracy and robustness.  
- Trained using **Scikit-learn** with hyperparameter tuning.  
- Achieved **high precision & recall** for banknote classification.  

📊 **Model Performance:**  
✅ **Accuracy:** 99%  
✅ **Precision & Recall:** Optimized for fraud detection  

---

## **6. API Development & Endpoints**  
This API is built using **FastAPI**, a high-performance framework for serving ML models.  

### 📡 **API Endpoints**  
#### ✅ **Home Endpoint**  
`GET /` → Returns a welcome message.  
📤 **Response (JSON)**  
```json
{
    "Message": "Hello Stranger"
}
```

---

## **7. Future Work**  
- 🔹 Integrate Deep Learning Models for enhanced accuracy.
- 🔹 Deploy on Cloud Platforms like AWS or Google Cloud.
- 🔹 Improve Fraud Detection Strategies for financial institutions.
- 🔹 Implement Real-Time Streaming for authentication at scale.

## **8. Technologies Used**  
+ 🔹 Programming: Python
+ 🔹 Machine Learning: Scikit-learn, Random Forest Classifier
+ 🔹 Web Framework: FastAPI
+ 🔹 API Server: Uvicorn
+ 🔹 Containerization: Docker
+ 🔹 Data Handling: Pandas, NumPy
+ 🔹 Model Deployment: Pickle
