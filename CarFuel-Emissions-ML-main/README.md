# 🚗 **Car Fuel and Emissions Analysis**  

## **1. Introduction**  
Understanding vehicle fuel consumption and emissions is crucial for **environmental sustainability** and **regulatory compliance**. This project leverages **machine learning and data visualization** to analyze fuel efficiency trends, predict CO₂ emissions, and classify vehicles based on their impact.  

✅ **Predicts CO₂ emissions** based on vehicle characteristics.  
✅ **Clusters vehicles** based on emissions and fuel efficiency.  
✅ **Analyzes fuel economy trends** using historical vehicle data (2000-2013).  

This project provides **data-driven insights** for policymakers, manufacturers, and consumers to promote **fuel-efficient vehicles**.  

---

## **2. Background**  
The automobile industry faces growing pressure to **reduce CO₂ emissions** and improve **fuel efficiency**. Key challenges include:  

🔹 **Emissions Regulations** – Stricter government policies on vehicle emissions.  
🔹 **Fuel Economy Optimization** – Need for data-driven insights to enhance vehicle efficiency.  
🔹 **Consumer Awareness** – Helping buyers understand fuel-efficient vehicle choices.  

This project addresses these challenges by:  

✅ **Building machine learning models** to predict emissions and fuel efficiency.  
✅ **Identifying vehicle clusters** based on fuel economy and emissions data.  
✅ **Visualizing industry trends** to support better decision-making.  

---

## **3. Data Collection and Processing**  
### **📂 Dataset**  
The dataset includes **vehicle fuel consumption and emissions data** from **2000 to 2013**, containing:  

| Feature | Description |
|---------|------------|
| `year` | Year of vehicle manufacture |
| `manufacturer` | Name of the car manufacturer |
| `model` | Model of the car |
| `engine_capacity` | Engine size in liters |
| `fuel_type` | Type of fuel used (Petrol, Diesel, etc.) |
| `co2` | CO₂ emissions (g/km) |
| `urban_metric` | Fuel consumption in urban areas (L/100km) |
| `extra_urban_metric` | Fuel consumption in extra-urban areas (L/100km) |
| `combined_metric` | Overall fuel efficiency (L/100km) |
| `transmission_type` | Type of vehicle transmission |
| `fuel_cost_6000_miles` | Estimated fuel cost for 6,000 miles |

### **🛠️ Data Preprocessing Steps**  
✅ **Checked for missing values** and handled inconsistencies.  
✅ **Standardized numerical features** for better model performance.  
✅ **Encoded categorical variables** for machine learning compatibility.  

---

## **4. Exploratory Data Analysis (EDA)**  
📊 **Emissions Trends Over Time**  
- **Analyzed CO₂ emissions reductions** over different car models and years.  

📈 **Fuel Efficiency vs. Engine Capacity**  
- **Scatter plots examined** how engine size affects fuel economy.  

📉 **Vehicle Clustering Analysis**  
- **Used KMeans to group vehicles** based on emissions and efficiency metrics.  

---

## **5. Model Development**  
### **📌 Machine Learning Models Used**  
#### **1️⃣ CO₂ Emissions Prediction**  
- **Model:** Linear Regression  
- **Objective:** Predict **CO₂ emissions** based on vehicle attributes.  

#### **2️⃣ Vehicle Clustering**  
- **Model:** KMeans Clustering  
- **Objective:** Identify **clusters of vehicles** based on fuel efficiency and emissions.  

#### **3️⃣ Fuel Efficiency Prediction**  
- **Model:** Random Forest Regression  
- **Objective:** Predict **vehicle fuel efficiency (combined metric)** based on attributes like engine capacity, fuel type, and urban/extra urban consumption.  

### **🛠 Model Training Process**  
✅ **Trained models on historical vehicle data** from 2000-2013.  
✅ **Optimized hyperparameters** for improved accuracy.  
✅ **Evaluated models using standard performance metrics.**  

---

## **6. Model Evaluation & Results**  
📊 **Performance Metrics:**  
✅ **R² Score** – Measures how well the model explains variations in emissions and fuel efficiency.  
✅ **Mean Absolute Error (MAE)** – Captures the average prediction error.  
✅ **Silhouette Score (for clustering)** – Evaluates cluster quality.  

📉 **Key Findings:**  
- **Engine size and fuel type are major determinants of CO₂ emissions.**  
- **Vehicles with automatic transmission tend to have slightly higher fuel consumption.**  
- **Hybrid and smaller-engine vehicles have significantly better fuel efficiency.**  

---

## **7. Visualizing the Results**  
📊 **Predicted vs. Actual CO₂ Emissions**  
- **Line plots & scatter plots** compared model predictions with actual emissions data.  

📈 **Cluster Visualization**  
- **KMeans clustering grouped vehicles** based on emissions and efficiency.  

📉 **Feature Importance Analysis**  
- **Bar plots highlighted the most influential factors** for predicting fuel consumption.  

---

## **8. Future Work**  
+ 🔹 Incorporate **Deep Learning models** for better fuel efficiency predictions.  
+ 🔹 Include **electric and hybrid vehicles** for a modern fuel economy analysis.  
+ 🔹 Develop an **interactive dashboard** for real-time vehicle emission analysis.  
+ 🔹 Expand dataset to include **real-world driving conditions** instead of lab-measured values.  

---

## **9. Technologies Used**  
+ 🔹 Programming: Python  
+ 🔹 Machine Learning: Scikit-learn (Linear Regression, Random Forest, KMeans Clustering)  
+ 🔹 Data Processing: Pandas, NumPy  
+ 🔹 Data Visualization: Seaborn, Matplotlib  
+ 🔹 Model Evaluation: R² Score, MAE, Silhouette Score  

---

## **10. Connect With Me**  
💼 **LinkedIn:** [Uvietobore Joshua Adjugah](https://www.linkedin.com/in/uvietobore-joshua-adjugah-2b548621a)  
📧 **Email:** uviejosh@gmail.com  

🚀 **Star this repo if you find it useful!** ⭐  
