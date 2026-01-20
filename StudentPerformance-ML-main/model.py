import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from keras._tf_keras.keras.layers import Dense
from keras._tf_keras.keras.models import Sequential
from keras._tf_keras.keras.optimizers import Adam
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score

# Load dataset from a CSV file
student_data = pd.read_csv("StudentPerformanceFactors.csv")

# Separate features (input variables) from target (output variable)
features = student_data.drop(columns='Exam_Score')  # Drop the target column to get features
score = student_data['Exam_Score']  # Target variable

# Fill NaN values with the mode of each column
features['Teacher_Quality'].fillna(features['Teacher_Quality'].mode()[0], inplace=True)
features['Parental_Education_Level'].fillna(features['Parental_Education_Level'].mode()[0], inplace=True)
features['Distance_from_Home'].fillna(features['Distance_from_Home'].mode()[0], inplace=True)

# Convert categorical features to one-hot encoded format
features = pd.get_dummies(features)

# Save the feature column names for later reference
feature_columns = features.columns

# Convert all data to float32 to ensure compatibility with TensorFlow
features = features.astype(np.float32)  # Convert feature data to float32
score = score.astype(np.float32)  # Convert target data to float32

# Split the data into training and testing sets (80% training, 20% testing)
features_train, features_test, score_train, score_test = train_test_split(features, score, test_size=0.2)

# Build and train a Random Forest Regressor
rf_model = RandomForestRegressor(n_estimators=200, random_state=42)  # Initialize Random Forest model with 200 trees
rf_model.fit(features_train, score_train)  # Train the model on the training data

# Calculate feature importance from the Random Forest model
importances = rf_model.feature_importances_  # Get feature importances
sorted_idx = np.argsort(importances)[::-1]  # Sort features by importance in descending order

# Print the top 10 most important features
print("Feature Importance Ranking (Random Forest):")
for i in sorted_idx[:10]:
    print(f"{feature_columns[i]}: {importances[i]}")

# Build a Neural Network model using Keras
model = Sequential()
model.add(Dense(16, input_dim=len(features.columns), activation='relu'))  # Input layer with 16 neurons
model.add(Dense(32, activation='relu'))  # Hidden layer with 32 neurons
model.add(Dense(32, activation='relu'))  # Hidden layer with 32 neurons
model.add(Dense(64, activation='relu'))  # Hidden layer with 64 neurons
model.add(Dense(64, activation='relu'))  # Hidden layer with 64 neurons
model.add(Dense(1, activation='linear'))  # Output layer with linear activation for regression

# Compile the Neural Network model
opt = Adam(learning_rate=0.00005)  # Adam optimizer with a learning rate of 0.00005
model.compile(
    metrics=['mse'],  # Use Mean Squared Error as a metric for regression
    loss='mean_squared_error',  # Loss function for regression
    optimizer=opt
)

# Train the Neural Network model on the training data
model.fit(features_train, score_train, epochs=200, batch_size=32, verbose=2)  # Train for 200 epochs

# Predict scores on the test set
model_result = np.array(model.predict(features_test))  # Predict exam scores
real_result = np.array(score_test)  # Convert test scores to numpy array

# Calculate R-squared (R²) score between the predicted and actual exam scores
r_squared = r2_score(real_result, model_result)

# Print R-squared value
print(f"R-squared: {r_squared:.4f}")

# Plot predicted scores vs. real scores for the first 100 test samples
plt.scatter(model_result[:100], real_result[:100], c='green')  # Scatter plot of predicted vs real scores
plt.xlabel('Exam Score')
plt.ylabel('Predicted Score')
plt.title('Predicted Score vs Real Score')
plt.grid(True)
plt.show()
