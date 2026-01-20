# 🚗 **Car Selling Price Prediction**  

## **1. Introduction**  
Determining the **optimal selling price of a car** is crucial for buyers, sellers, and dealerships. This project builds a **predictive model** using **Random Forest Regressor** to estimate a car’s selling price based on various features.  

✅ **Preprocessed and cleaned car data** for better model accuracy.  
✅ **Trained a Random Forest model** to predict car selling prices.  
✅ **Evaluated model performance** using industry-standard regression metrics.  

This project provides valuable insights into **pricing strategies** by analyzing key factors that influence car value.  

---

## **2. Background**  
Car pricing is influenced by multiple factors, including:  

🔹 **Depreciation Trends** – Older cars lose value over time.  
🔹 **Market Demand** – Certain brands and models retain higher resale value.  
🔹 **Feature Influence** – Mileage, fuel type, transmission, and previous ownership affect pricing.  

This project addresses these challenges by:  

✅ **Applying machine learning to predict car prices** accurately.  
✅ **Analyzing key features** that influence a car’s market value.  
✅ **Visualizing relationships between features and selling prices**.  

---

## **3. Data Collection and Processing**  
### **📂 Dataset**  
The dataset **car_data.csv** contains historical car selling prices along with relevant features.  

| Feature | Description |
|---------|------------|
| `Year` | Manufacturing year of the car |
| `Selling_Price` | Target variable – actual selling price of the car |
| `Present_Price` | Showroom price of the car |
| `Kms_Driven` | Total distance the car has been driven |
| `Fuel_Type` | Type of fuel used (Petrol/Diesel/CNG) |
| `Transmission` | Type of gearbox (Manual/Automatic) |
| `Owner` | Number of previous owners |

### **🛠️ Data Preprocessing Steps**  
✅ **Encoded categorical features** using `LabelEncoder`.  
✅ **Performed feature scaling** for numerical variables.  
✅ **Split dataset into training (80%) and testing (20%) sets**.  

---

## **4. Exploratory Data Analysis (EDA)**  
📊 **Correlation Analysis**  
- **Heatmaps** revealed how features like `Year`, `Present_Price`, and `Fuel_Type` impact selling price.  

📉 **Feature Importance Analysis**  
- **Bar plots** visualized the influence of each variable on car pricing.  

📈 **Price Trends Over Time**  
- **Line plots** examined price depreciation patterns based on `Year`.  

---

## **5. Model Development**  
### **📌 Machine Learning Model Used**  
- **Random Forest Regressor** 🌳 – Chosen for its ability to handle **non-linear relationships** in car pricing.  

### **🛠 Model Training Process**  
✅ **Trained Random Forest on preprocessed data**.  
✅ **Performed hyperparameter tuning** to optimize accuracy.  
✅ **Evaluated using regression performance metrics**.  

---

## **6. Model Evaluation & Results**  
📊 **Performance Metrics:**  
✅ **R² Score** – Measures how well the model explains price variation.  
✅ **Mean Absolute Error (MAE)** – Captures average prediction error.  
✅ **Root Mean Squared Error (RMSE)** – Highlights variance in predictions.  
✅ **Cross-Validation Score** – Ensures model generalizability.  

📉 **Key Findings:**  
- **Recent models with fewer previous owners had higher resale values.**  
- **Diesel cars retained their value better than petrol variants.**  
- **Automatic cars generally had higher selling prices than manual ones.**  

---

## **7. Visualizing the Results**  
📊 **Comparison of Predicted vs. Actual Prices**  
- **Scatter Plots** – Compared model predictions with actual selling prices.  
- **Line Charts** – Analyzed price trends over different car models.  

📈 **Feature Influence Analysis**  
- **Bar plots** showcased the most influential factors in price determination.  
- **Heatmaps** illustrated correlation patterns between features.  

---

## **8. Future Work**  
+ 🔹 Test additional regression models (XGBoost, Gradient Boosting) for better accuracy.  
+ 🔹 Expand dataset with **real-time car market data** from dealerships and online listings.  
+ 🔹 Develop an API for **instant car price predictions** based on user inputs.  
+ 🔹 Integrate web scraping for automatic car listing data collection.  

---

## **9. Technologies Used**  
+ 🔹 Programming: Python  
+ 🔹 Machine Learning: Scikit-learn, Random Forest Regressor  
+ 🔹 Data Processing: Pandas, NumPy  
+ 🔹 Data Visualization: Seaborn, Matplotlib  
+ 🔹 Model Evaluation: R² Score, MAE, RMSE, Cross-Validation  

---

## **10. Connect With Me**  
💼 **LinkedIn:** [Uvietobore Joshua Adjugah](https://www.linkedin.com/in/uvietobore-joshua-adjugah-2b548621a)  
📧 **Email:** uviejosh@gmail.com  

🚀 **Star this repo if you find it useful!** ⭐  
