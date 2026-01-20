# 📈 **Predicting Customer Satisfaction with Machine Learning**  

## **1. Introduction**  
Understanding customer satisfaction is vital for enhancing business strategies and creating **impactful customer experiences**. This project leverages the **Customer Feedback and Satisfaction Dataset** to develop a **predictive model** that forecasts satisfaction scores based on demographic and behavioral features of **38,444 customers**.  

✅ **Predict satisfaction levels** using machine learning.  
✅ **Analyze key factors** influencing customer happiness.  
✅ **Generate actionable insights** for business growth.  

---

## **2. Background**  
Customer satisfaction impacts **brand loyalty, revenue, and retention**. However, businesses face challenges in accurately predicting satisfaction due to:  

🔹 **Complex Customer Behavior** – Satisfaction is influenced by multiple **interconnected factors**.  
🔹 **Ineffective Feedback Utilization** – Businesses collect vast amounts of customer feedback but **struggle to extract insights**.  
🔹 **Lack of Predictive Insights** – Traditional methods **fail to provide real-time satisfaction forecasts**.  

This project addresses these issues by:  

✅ **Building a regression model** to predict customer satisfaction.  
✅ **Identifying top predictors** such as **loyalty level, feedback score, and demographics**.  
✅ **Providing businesses with data-driven recommendations** to improve customer experience.  

---

## **3. Data Collection and Processing**  
### **📂 Dataset**  
This dataset contains key **demographic and behavioral** attributes affecting satisfaction:  

| Feature | Description |
|---------|------------|
| `age` | Age of the customer |
| `gender` | Male/Female |
| `country` | Customer’s location |
| `loyalty_level` | Loyalty program tier |
| `feedback_score` | Customer's feedback rating |
| `purchase_frequency` | Number of purchases per month |
| **Target (`satisfaction_score`)** | Customer satisfaction rating (0-100) |

### **🛠️ Data Preprocessing Steps**  
✅ **Encoded categorical variables** using One-Hot Encoding.  
✅ **Scaled numerical features** using MinMax Scaler.  
✅ **Applied Principal Component Analysis (PCA)** to reduce dimensionality while preserving **95% variance**.  

---

## **4. Exploratory Data Analysis (EDA)**  
📊 **Correlation Analysis**  
- **Loyalty level and feedback score** showed strong correlation with satisfaction.  
- **Customers with higher loyalty levels** had consistently higher satisfaction ratings.  

📈 **Feature Distributions**  
- Analyzed **satisfaction trends by age, country, and purchase behavior**.  
- **Scatter plots & box plots** provided insights into satisfaction variations.  

---

## **5. Model Development**  
### **📌 Machine Learning Model Used**  
- **Support Vector Regression (SVR)** 🛠️ – Chosen for handling **non-linear relationships** in customer data.  
- **Hyperparameter Tuning:**  
  - **Kernel:** RBF  
  - **C:** 10, **ε:** 0.5  

---

## **6. Business Insights & Results**  
🔹 **Loyalty level was the strongest predictor** of satisfaction.  
🔹 Customers who provided **higher feedback scores** had **better overall experiences**.  
🔹 **Actionable recommendation:** Brands should **enhance loyalty programs** and **collect structured feedback** for better customer retention.  

---

## **7. Future Work**  
+ 🔹 Implement Deep Learning models (e.g., Neural Networks) for advanced prediction.
+ 🔹 Expand dataset with additional behavioral factors like engagement metrics.
+ 🔹 Develop an API for real-time customer satisfaction scoring.
+ 🔹 Deploy model using Flask/FastAPI for integration with business platforms.

---

## **8. Technologies Used**  
+ 🔹 Programming: Python
+ 🔹 Machine Learning: Scikit-learn, Support Vector Regression (SVR)
+ 🔹 Data Processing: Pandas, NumPy
+ 🔹 Data Visualization: Seaborn, Matplotlib
+ 🔹 Model Evaluation: R² Score, MAE, RMSE

---

## **9. Connect With Me**  
💼 **LinkedIn:** [Uvietobore Joshua Adjugah](https://www.linkedin.com/in/uvietobore-joshua-adjugah-2b548621a)  
📧 **Email:** uviejosh@gmail.com  

