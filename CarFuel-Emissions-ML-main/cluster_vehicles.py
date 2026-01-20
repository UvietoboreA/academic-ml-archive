import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import silhouette_score
from sklearn.cluster import KMeans

# Load the dataset
data = pd.read_csv('CarFuelandEmissions2000_2013.csv', low_memory=False)

# Drop irrelevant columns from the dataset
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

# Select the features to use for clustering
features_to_use = ['co2', 'combined_metric']
features = data[features_to_use]

# If there are any categorical columns, convert them into dummy/one-hot encoded variables
features = pd.get_dummies(features, drop_first=True)

# Convert features into numpy array for clustering
features_array = features.values

# List of k values to test (from 1 to 10 clusters)
k_values = range(1, 11)
inertia_list = []

# Loop through different values of k and calculate inertia (sum of squared distances)
for k in k_values:
    model = KMeans(n_clusters=k, random_state=42)
    model.fit(features_array)
    inertia_list.append(model.inertia_)

# Plot the Elbow Curve to determine the optimal k value
plt.figure(figsize=(8, 5))
plt.plot(k_values, inertia_list, marker='o')
plt.xlabel('Number of Clusters (k)')
plt.ylabel('Inertia (Sum of Squared Distances)')
plt.title('Elbow Method for Optimal k')
plt.grid(True)
plt.show()

# Using KMeans with an optimal number of clusters (e.g., k=4)
optimal_k = 4
kmeans_model = KMeans(n_clusters=optimal_k, random_state=42)
kmeans_model.fit(features_array)

# Predict cluster labels for each data point
labels = kmeans_model.labels_

# Calculate Silhouette Score to evaluate the quality of the clusters
silhouette_avg = silhouette_score(features_array, labels)
print(f'Silhouette Score for k={optimal_k}: {silhouette_avg:.3f}')

# Add the cluster labels back to the original data
data['cluster'] = labels

print(data[data['cluster'] == 0])               #First Cluster
print(data[data['cluster'] == 1])               #Second Cluster
print(data[data['cluster'] == 2])               #Third Cluster
print(data[data['cluster'] == 3])               #Fourth Cluster


# Visualize the clusters with a scatter plot
plt.figure(figsize=(8, 6))
plt.scatter(features_array[:, 0], features_array[:, 1], c=labels, cmap='viridis', marker='o')
plt.xlabel('CO2 Emissions')
plt.ylabel('Combined Metric')
plt.title(f'Clusters for k={optimal_k}')
plt.colorbar(label='Cluster')
plt.grid(True)
plt.show()
