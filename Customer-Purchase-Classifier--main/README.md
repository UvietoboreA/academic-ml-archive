# 🔍📊 **Building a Decision Tree Classifier to Predict Customer Purchases**  

## **1. Introduction**  
Understanding customer purchasing behavior is essential for optimizing **marketing strategies, sales forecasting, and product recommendations**. This project focuses on building a **Decision Tree Classifier** to predict whether a customer will purchase a product based on various factors.  

✅ **Preprocessed customer data** to enhance model performance.  
✅ **Built a Decision Tree model** for purchase prediction.  
✅ **Evaluated model accuracy** and identified key decision-making factors.  

This project provides insights into **customer purchase patterns**, enabling businesses to **improve marketing efficiency** and **increase conversion rates**.  

---

## **2. Background**  
Businesses face challenges in **predicting customer behavior**, such as:  

🔹 **Unstructured Customer Data** – Data needs **cleaning and preprocessing** before model training.  
🔹 **High Dimensionality** – Identifying **key purchase factors** requires **feature selection**.  
🔹 **Overfitting in Decision Trees** – Proper hyperparameter tuning is required for **generalizability**.  

This project addresses these challenges by:  

✅ **Applying data preprocessing techniques** for structured input.  
✅ **Building a Decision Tree Classifier** optimized with entropy-based splits.  
✅ **Using feature importance analysis** to determine key drivers of customer purchases.  

---

## **3. Data Collection and Processing**  
### **📂 Dataset**  
The dataset contains **customer demographics, behavioral attributes, and purchase decisions**.  

| Feature | Description |
|---------|------------|
| `age` | Age of the customer |
| `gender` | Male/Female |
| `income` | Annual income bracket |
| `product_interest` | Category of product viewed |
| `purchase` | Target variable (1 = Purchased, 0 = Not Purchased) |

### **🛠️ Data Preprocessing Steps**  
✅ **Encoded categorical variables** using **LabelEncoder**.  
✅ **Scaled numerical features** using **MinMaxScaler** for uniform value distribution.  
✅ **Split dataset** into **training (80%) and testing (20%) sets**.  

---

## **4. Exploratory Data Analysis (EDA)**  
📊 **Feature Correlation Analysis**  
- **Customer income and product interest** were key predictors of purchases.  
- **Gender had minimal impact**, but **age correlated with certain product categories**.  

📈 **Purchase Trends Visualization**  
- **Heatmaps & bar plots** showed customer purchasing behavior across different demographics.  

---

## **5. Model Development**  
### **📌 Machine Learning Model Used**  
- **Decision Tree Classifier** 🌳 – Used for its **interpretability and rule-based decision-making**.  
- **Hyperparameters Optimized:**  
  - **Criterion:** Entropy  
  - **Max Depth:** 13  
  - **Min Samples Split:** 25  

📊 **Model Performance:**  
✅ **Accuracy Score:** Evaluated using **train-test split**.  
✅ **Confusion Matrix:** Visualized **false positives and false negatives**.  
✅ **Cross-Validation:** Assessed model generalizability.  

---

## **6. Business Insights & Results**  
🔹 **Customer income level played the most significant role** in purchase decisions.  
🔹 **Product category preference impacted purchases more than gender**.  
🔹 **Feature importance analysis helped refine customer targeting strategies**.  
🔹 **Actionable recommendation:** Businesses should **tailor marketing campaigns** based on income and product interest trends.  

---

## **7. Future Work**  
+ 🔹 Implement ensemble methods (Random Forest, XGBoost) for better accuracy.
+ 🔹 Expand dataset with customer interaction metrics (click-through rates, session durations).
+ 🔹 Develop an API to integrate purchase prediction models into e-commerce platforms.
+ 🔹 Test model performance on different customer demographics for broader insights.

---

## **8. Technologies Used**  
+ 🔹 Programming: Python
+ 🔹 Machine Learning: Scikit-learn, Decision Tree Classifier
+ 🔹 Data Processing: Pandas, NumPy
+ 🔹 Data Visualization: Seaborn, Matplotlib
+ 🔹 Model Evaluation: Accuracy, Confusion Matrix, Feature Importance

---

## **9. Connect With Me**  
💼 **LinkedIn:** [Uvietobore Joshua Adjugah](https://www.linkedin.com/in/uvietobore-joshua-adjugah-2b548621a)  
📧 **Email:** uviejosh@gmail.com  

🚀 **Star this repo if you find it useful!** ⭐  
