# 📈 **Sales Prediction Using Multiple Regression Models**  

## **1. Introduction**  
Advertising plays a critical role in driving sales, but **which platform contributes the most to revenue?** This project builds a **Sales Prediction Model** using **Multiple Regression Techniques** to analyze the impact of advertising spend across **TV, Radio, and Newspaper** channels.  

✅ **Predicts sales based on ad spending** across different platforms.  
✅ **Compares multiple regression models** to determine the most effective approach.  
✅ **Evaluates performance using R² Score, MAE, RMSE, and Cross-Validation.**  

This project provides **data-driven insights** for **optimizing marketing budgets** and **maximizing sales impact**.  

---

## **2. Background**  
Marketing teams often struggle to allocate budgets effectively because:  

🔹 **Unclear ROI of Advertising Channels** – TV, Radio, and Newspaper contribute differently to sales.  
🔹 **Fluctuating Customer Behavior** – Trends change, requiring **data-driven forecasting**.  
🔹 **Choosing the Best Model** – Selecting an accurate and explainable prediction model is crucial.  

This project addresses these challenges by:  

✅ **Building multiple regression models** to forecast sales based on advertising spend.  
✅ **Comparing model performance** to determine the best prediction method.  
✅ **Visualizing trends** for **data-driven marketing decisions**.  

---

## **3. Data Collection and Processing**  
### **📂 Dataset**  
The dataset **Advertising.csv** contains advertising spend data and corresponding sales figures.  

| Feature | Description |
|---------|------------|
| `TV` | Advertising spend on TV |
| `Radio` | Advertising spend on Radio |
| `Newspaper` | Advertising spend on Newspapers |
| `Sales` | Sales generated as a result of advertising |

### **🛠️ Data Preprocessing Steps**  
✅ **Renamed columns** for better readability.  
✅ **Dropped unnecessary columns (`Id`)** to avoid redundancy.  
✅ **Checked for missing values** and handled inconsistencies.  

---

## **4. Exploratory Data Analysis (EDA)**  
📊 **Correlation Analysis**  
- **Heatmaps** visualized relationships between ad spend and sales.  
- **TV advertising** showed the highest correlation with sales.  

📈 **Feature Distributions & Trends**  
- **Histograms** revealed spending patterns across platforms.  
- **Scatter plots** analyzed how each platform influenced sales.  

📉 **Pairwise Relationships**  
- **Pair plots** provided insights into the relationship between variables.  

---

## **5. Model Development**  
### **📌 Machine Learning Models Used**  
To **predict sales based on ad spending**, five regression models were trained and compared:  

- **Linear Regression** 📈 – Standard approach for sales prediction.  
- **Ridge Regression** 🔵 – Regularized version to prevent overfitting.  
- **Lasso Regression** 🟡 – Feature selection by reducing less important coefficients.  
- **Random Forest Regressor** 🌲 – Captures non-linear relationships.  
- **Decision Tree Regressor** 🌳 – Splits data into decision rules for predictions.  

### **🛠 Model Training Process**  
✅ **Split dataset** into **training (70%) and testing (30%) sets**.  
✅ **Trained each regression model** on the preprocessed dataset.  
✅ **Evaluated model performance** using multiple metrics.  

---

## **6. Model Evaluation & Results**  
📊 **Performance Metrics:**  
Each model was assessed based on:  

✅ **R² Score** – Measures how well the predictions match the actual values.  
✅ **Mean Absolute Error (MAE)** – Measures the average prediction error.  
✅ **Root Mean Squared Error (RMSE)** – Captures variance in prediction errors.  
✅ **Cross-Validation Score** – Evaluates model consistency across different datasets.  

📉 **Key Findings:**  
- **TV advertising had the highest impact on sales**, followed by Radio.  
- **Newspaper ads contributed the least** to overall revenue.  
- **Random Forest performed best**, capturing non-linear patterns in the data.  

---

## **7. Visualizing the Results**  
📊 **Comparison of Model Performance**  
- **Bar Plots** – Compared MAE, RMSE, and R² scores across models.  
- **Line Plots** – Showed actual vs. predicted sales trends.  
- **Scatter Plots** – Visualized the relationship between **predicted and actual sales** for each model.  

📈 **Key Takeaways:**  
✅ **TV and Radio spending showed strong predictive power** in driving sales.  
✅ **Non-linear models (Random Forest, Decision Tree) captured patterns better than traditional regression models.**  
✅ **Data visualization enabled clear comparison of model accuracy and effectiveness.**  

---

## **8. Future Work**  
+ 🔹 Test additional **ensemble models** like Gradient Boosting for better accuracy.  
+ 🔹 Expand dataset with **digital ad spending (social media, search engine ads)**.  
+ 🔹 Develop a **real-time sales prediction dashboard** for marketing teams.  
+ 🔹 Automate feature selection for more efficient model tuning.  

---

## **9. Technologies Used**  
+ 🔹 Programming: Python  
+ 🔹 Machine Learning: Scikit-learn, Ridge Regression, Lasso Regression, Random Forest  
+ 🔹 Data Processing: Pandas, NumPy  
+ 🔹 Data Visualization: Seaborn, Matplotlib  
+ 🔹 Model Evaluation: R² Score, MAE, RMSE, Cross-Validation  

---

## **10. Connect With Me**  
💼 **LinkedIn:** [Uvietobore Joshua Adjugah](https://www.linkedin.com/in/uvietobore-joshua-adjugah-2b548621a)  
📧 **Email:** uviejosh@gmail.com  

🚀 **Star this repo if you find it useful!** ⭐  
