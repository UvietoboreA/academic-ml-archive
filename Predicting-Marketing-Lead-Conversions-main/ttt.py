import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import LabelEncoder, MinMaxScaler
from sklearn.model_selection import cross_val_score
from sklearn.metrics import make_scorer, mean_absolute_error

# Data columns setup
categorical_columns = ['Industry', 'Pitch', 'Fund_category', 'Geography', 'Designation', 'Hiring_candidate_role', 
                       'Lead_source', 'Level_of_meeting', 'Resource', 'Location', 'Last_lead_update', 'Internal_POC']
drop = ['Deal_title', 'Date_of_creation', 'Contact_no', 'Lead_name', 'POC_name', 'Lead_POC_email']
money_columns = ['Deal_value', 'Weighted_amount']
num_columns = ['Internal_rating', 'Lead_revenue']
all_num = money_columns + num_columns

# Load training data
train_data = pd.read_csv('train.csv')

# Prepare features and target
features_train = train_data.drop(columns=drop + ['Success_probability'])
target_train = train_data['Success_probability']

# Conversion functions for revenue
def convert_to_numeric(value):
    value = value.strip().lower()
    if '-' in value:
        low, high = value.split('-')
        return (parse_value(low) + parse_value(high)) / 2
    return parse_value(value)

def parse_value(value):
    if 'million' in value:
        return float(value.replace('million', '').strip()) * 1_000_000
    elif 'billion' in value:
        return float(value.replace('billion', '').strip()) * 1_000_000_000
    else:
        return float(value)

# Apply conversion and fill missing values for categorical columns in training data
train_data['Lead_revenue'] = train_data['Lead_revenue'].apply(convert_to_numeric)
for column in categorical_columns:
    train_data[column] = train_data[column].fillna(train_data[column].mode()[0])

# Encoding categorical variables with LabelEncoder
label_encoders = {}
for column in categorical_columns:
    le = LabelEncoder()
    train_data[column] = le.fit_transform(train_data[column])
    label_encoders[column] = le  # Save encoder for future use

# Convert money columns to float and fill missing values
for column in money_columns:
    train_data[column] = train_data[column].replace({'\\$': '', ',': ''}, regex=True).astype(float)
for column in all_num:
    train_data[column] = train_data[column].fillna(train_data[column].mean())

# Scaling numeric columns
mmax = MinMaxScaler()
train_data[all_num] = mmax.fit_transform(train_data[all_num])

# Prepare the features and target for model fitting
features_train = train_data.drop(columns=drop + ['Success_probability'])


# Define models
model_1 = RandomForestRegressor(
                                n_estimators=450,
                                criterion='absolute_error',
                                max_depth=18,
                                min_samples_split=7,
                                min_samples_leaf=7,
                                max_features=3,
                                n_jobs=-1,
                                random_state=42,
                                verbose=2     
                                )

model_2 = DecisionTreeRegressor(
                                criterion='absolute_error',
                                splitter='random',
                                max_depth=17,
                                min_samples_split=6,
                                min_samples_leaf=6,
                                max_features=3
                                )

# Fit models
fitted_1 = model_1.fit(features_train, target_train)
fitted_2 = model_2.fit(features_train, target_train)

# Load test data
test_data = pd.read_csv('test.csv')
test_data = test_data.drop(columns=drop)

# Apply revenue conversion and fill missing values for test data
test_data['Lead_revenue'] = test_data['Lead_revenue'].apply(convert_to_numeric)
for column in categorical_columns:
    test_data[column] = test_data[column].fillna(train_data[column].mode()[0])

# Encoding categorical variables in test data using trained LabelEncoders
for column in categorical_columns:
    le = label_encoders[column]
    # Map unseen labels to -1 or other placeholder
    test_data[column] = test_data[column].apply(lambda x: le.transform([x])[0] if x in le.classes_ else -1)

# Convert money columns to float and fill missing values in test data
for column in money_columns:
    test_data[column] = test_data[column].replace({'\\$': '', ',': ''}, regex=True).astype(float)

# Fill missing values in numeric columns
for column in all_num:
    test_data[column] = test_data[column].fillna(train_data[column].mean())

# Apply MinMaxScaler from training to test data
test_data[all_num] = mmax.transform(test_data[all_num])

# Prepare test features
features_test = test_data.copy()

# Make predictions with each model
pred_rf = fitted_1.predict(features_test)
pred_dt = fitted_2.predict(features_test)

# Print predictions
print("Random Forest Predictions:", pred_rf)
print("Decision Tree Predictions:", pred_dt)

# Define a scorer for MAE and MSE (you can also use other metrics)
mae_scorer = make_scorer(mean_absolute_error)

# Perform cross-validation on each model
scores_rf = cross_val_score(model_1, features_train, target_train, cv=5, scoring=mae_scorer)
scores_dt = cross_val_score(model_2, features_train, target_train, cv=5, scoring=mae_scorer)
print("Cross-Validated MAE for Random Forest:", scores_rf.mean())
print("Cross-Validated MAE for Decision Tree:", scores_dt.mean())

# Set up seaborn style
sns.set_theme(style="whitegrid")

# Visualization 1: Feature Importances for Random Forest
# Get feature importances from the Random Forest model
feature_importances = fitted_1.feature_importances_
features = features_train.columns
importance_df = pd.DataFrame({"Feature": features, "Importance": feature_importances})
importance_df = importance_df.sort_values(by="Importance", ascending=False)

# Plot Feature Importances
plt.figure(figsize=(12, 6))
sns.barplot(x="Importance", y="Feature", data=importance_df)
plt.title("Feature Importances from Random Forest Model")
plt.show()

# Visualization 2: Cross-Validation MAE Scores Comparison
cv_results = pd.DataFrame({
    "Model": ["Random Forest"] * len(scores_rf) + ["Decision Tree"] * len(scores_dt),
    "MAE Score": np.concatenate((scores_rf, scores_dt))
})

plt.figure(figsize=(10, 5))
sns.histplot(x="Model", y="MAE Score", data=cv_results, palette="Set2", hue="Model", legend=False)
plt.title("Cross-Validation Mean Absolute Error (MAE) Scores by Model")
plt.show()

# Visualization 3: Prediction Distributions for Random Forest and Decision Tree
plt.figure(figsize=(12, 6))
sns.kdeplot(pred_rf, label="Random Forest Predictions", color="blue")
sns.kdeplot(pred_dt, label="Decision Tree Predictions", color="green")
plt.title("Distribution of Predictions for Random Forest and Decision Tree")
plt.xlabel("Predicted Success Probability")
plt.legend()
plt.show()
