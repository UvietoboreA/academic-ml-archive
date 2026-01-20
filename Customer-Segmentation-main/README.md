# 🚀 **Customer Segmentation with Machine Learning: Driving Strategic Market Expansion**  

## **1. Introduction**  
An **automobile company** is expanding into **new markets** with its existing products (**P1, P2, P3, P4, and P5**). The goal is to classify **2,627 potential customers** into **four customer segments (A, B, C, D)** using **machine learning**.  

By leveraging **classification models**, we can **optimize marketing strategies** and **tailor customer outreach**, ensuring a **data-driven approach** to market expansion.  

✅ **Understand customer behaviors** to refine product positioning.  
✅ **Enhance strategic marketing** by targeting specific customer segments.  
✅ **Use data-driven insights** to improve decision-making.  

---

## **2. Background**  
Traditional marketing segmentation often relies on **manual analysis** and **demographic insights**, leading to **suboptimal customer classification**. Key challenges include:  

🔹 **Inefficient Customer Targeting** – Broad market strategies lead to **higher marketing costs**.  
🔹 **Lack of Personalized Outreach** – Generic campaigns fail to **resonate with specific customer groups**.  
🔹 **Data Overload Without Insights** – Businesses struggle to **extract value from raw customer data**.  

This project tackles these challenges by:  

✅ **Building a classification model** to segment customers.  
✅ **Identifying key characteristics** that define each segment.  
✅ **Providing actionable recommendations** for marketing and product alignment.  

---

## **3. Data Collection and Processing**  
### **📂 Dataset**  
The dataset includes key attributes influencing **customer segmentation**:  

| Feature | Description |
|---------|------------|
| `age` | Customer's age |
| `gender` | Male/Female |
| `marital_status` | Single/Married/Divorced |
| `profession` | Occupation category |
| `spending_score` | Customer spending behavior (0-100) |
| `family_size` | Number of family members |
| `segment` | Target variable (A, B, C, D) |

### **🛠️ Data Preprocessing Steps**  
✅ **Handled Missing Data** – Used **mode imputation** for categorical and **median imputation** for numerical values.  
✅ **Feature Encoding** – Applied **One-Hot Encoding** for categorical features.  
✅ **Feature Scaling** – Used **MinMax Scaling** to normalize numerical values.  

---

## **4. Exploratory Data Analysis (EDA)**  
📊 **Customer Demographics Analysis**  
- Examined **age, gender, and profession distributions** across segments.  
- Identified key differences in **spending behavior and family size**.  

📈 **Feature Importance Analysis**  
- Used **correlation heatmaps and box plots** to highlight variables affecting customer segmentation.  

---

## **5. Model Development**  
### **📌 Machine Learning Model Used**  
- **Decision Tree Classifier** 🌳 – Chosen for **interpretability and efficiency**.  
- **Hyperparameters Optimized**:  
  - **Criterion**: Entropy  
  - **Max Depth**: 8  

📊 **Model Performance:**  
✅ **Accurately predicted customer segments (A, B, C, D)**.  
✅ **Provided interpretable insights** for strategic decision-making.  

---

## **6. Business Insights & Results**  
🔹 **Spending Score & Profession** were the **strongest predictors** of customer segment.  
🔹 **Segment A & B customers** had **higher spending scores**, making them **priority targets**.  
🔹 **Family size & marital status** played a role in differentiating customer groups.  

---

## **7. Future Work**  
+ 🔹 Implement additional ML models (e.g., K-Means Clustering) for unsupervised segmentation.
+ 🔹 Develop an API for real-time customer classification.
+ 🔹 Expand dataset to include purchase history for deeper insights.
+ 🔹 Integrate segmentation results into marketing automation tools.

---

## **8. Technologies Used**  
+ 🔹 Programming: Python
+ 🔹 Machine Learning: Scikit-learn, Decision Tree
+ 🔹 Data Processing: Pandas, NumPy
+ 🔹 Data Visualization: Seaborn, Matplotlib
+ 🔹 Model Evaluation: Classification Metrics

---

## **9. Connect With Me**  
💼 **LinkedIn:** [Uvietobore Joshua Adjugah](https://www.linkedin.com/in/uvietobore-joshua-adjugah-2b548621a)  
📧 **Email:** uviejosh@gmail.com  

