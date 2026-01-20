import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score

# Load the dataset
data = pd.read_csv('CarFuelandEmissions2000_2013.csv', low_memory=False)

# Drop irrelevant columns
columns_to_drop = [
    'file', 'co_emissions', 'tax_band', 'thc_emissions', 'nox_emissions', 
    'thc_nox_emissions', 'particulates_emissions', 'fuel_cost_12000_miles', 
    'standard_12_months', 'standard_6_months', 'first_year_12_months', 
    'first_year_6_months', 'date_of_change'
]
data = data.drop(columns_to_drop, axis=1)

# Fill missing values: use mean for numeric columns, 0 for others
for column in data.columns:
    if data[column].dtype in ['float64', 'int64']:
        data[column].fillna(data[column].mean(), inplace=True)
    else:
        data[column].fillna(0, inplace=True)

# Display the first few rows of the cleaned data
print(data.head())

# Select relevant columns for features and the target variable
features_columns = ['engine_capacity', 'fuel_type', 'urban_metric', 'extra_urban_metric', 'combined_metric']
features = data[features_columns]

# Convert categorical columns (like 'fuel_type') into numerical values using one-hot encoding
features = pd.get_dummies(features, drop_first=True)

# Set 'co2' as the target variable
target = data['co2']

# Split the dataset into training and testing sets (80% train, 20% test)
features_train, features_test, target_train, target_test = train_test_split(features, target, test_size=0.2, random_state=42)

# Initialize and train the Linear Regression model
model = LinearRegression()
model.fit(features_train, target_train)

# Predict CO2 emissions for the test set
target_pred = model.predict(features_test)

# Scatter plot of actual vs predicted CO2 emissions
plt.figure(figsize=(8, 6))
plt.scatter(target_test, target_pred, alpha=0.3)
plt.xlabel('Actual CO2 Emissions')
plt.ylabel('Predicted CO2 Emissions')
plt.title('Actual vs Predicted CO2 Emissions')
plt.grid(True)
plt.show()

# Evaluate the model using Mean Absolute Error (MAE) and R-squared score
mae = mean_absolute_error(target_test, target_pred)
r2 = r2_score(target_test, target_pred)

print(f"Mean Absolute Error (MAE): {mae:.2f}")
print(f"R-squared Score: {r2:.3f}")

# Display the model's coefficients and intercept
print("Model Coefficients:", model.coef_)
print("Intercept:", model.intercept_)

# Visualize the feature importance (model coefficients) as a horizontal bar chart
plt.figure(figsize=(8, 6))
plt.barh(features.columns, model.coef_, color='lightblue')
plt.xlabel('Coefficient Value')
plt.ylabel('Feature')
plt.title('Feature Importance for CO2 Emissions')
plt.grid(True)
plt.show()
