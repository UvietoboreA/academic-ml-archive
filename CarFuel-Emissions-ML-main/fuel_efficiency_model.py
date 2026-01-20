import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
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

# Fill missing values: Use mean for numeric columns and 0 for categorical ones
for column in data.columns:
    if data[column].dtype in ['float64', 'int64']:
        data[column].fillna(data[column].mean(), inplace=True)
    else:
        data[column].fillna(0, inplace=True)

# Display the first few rows of the cleaned dataset
print(data.head())

# Select relevant columns for features and the target variable
features_columns = ['engine_capacity', 'fuel_type', 'urban_metric', 'extra_urban_metric']
features = data[features_columns]

# Convert categorical columns (e.g., fuel_type) into numerical values using one-hot encoding
features = pd.get_dummies(features, drop_first=True)

# Set 'combined_metric' as the target variable (fuel efficiency)
target = data['combined_metric']

# Split the dataset into training and testing sets (80% train, 20% test)
features_train, features_test, target_train, target_test = train_test_split(features, target, test_size=0.2, random_state=42)

# Initialize and train the Random Forest Regressor model
model = RandomForestRegressor(random_state=42)
model.fit(features_train, target_train)

# Predict fuel efficiency for the test set
target_pred = model.predict(features_test)

# Plot actual vs predicted fuel efficiency
plt.figure(figsize=(8, 6))
plt.scatter(target_test, target_pred, alpha=0.3)
plt.xlabel('Actual Fuel Efficiency')
plt.ylabel('Predicted Fuel Efficiency')
plt.title('Actual vs Predicted Fuel Efficiency')
plt.grid(True)
plt.show()

# Calculate evaluation metrics: Mean Absolute Error (MAE) and R2 score
mae = mean_absolute_error(target_test, target_pred)
r2 = r2_score(target_test, target_pred)
print(f'Mean Absolute Error (MAE): {mae:.2f}')
print(f'R2 Score: {r2:.3f}')

# Calculate and plot feature importance from the Random Forest model
feature_importance = model.feature_importances_

# Plot a horizontal bar graph to visualize feature importance
plt.figure(figsize=(8, 6))
plt.barh(features.columns, feature_importance, color='skyblue')
plt.xlabel('Importance Score')
plt.ylabel('Feature')
plt.title('Feature Importance for Fuel Efficiency')
plt.grid(True)
plt.show()
