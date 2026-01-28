# K-Means Clustering Example
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler

# ---- Step 1: Load Dataset ----
iris = load_iris()
X = iris.data
y = iris.target # Actual labels (used only for evaluation)

# ---- Step 2: Standardize Features ----
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# ---- Step 3: Apply K-Means Algorithm ----
kmeans = KMeans(n_clusters=3, random_state=42)
kmeans.fit(X_scaled)

# ---- Step 4: Get Results ----
labels = kmeans.labels_
centroids = kmeans.cluster_centers_

print("\nCluster Centers (Standardized):")
print(centroids)
print("\nCluster Labels Assigned to Each Data Point:")
print(labels)

# ---- Step 5: Visualization (Using first two features) ----
plt.figure(figsize=(8, 6))
plt.scatter(X_scaled[:, 0], X_scaled[:, 1], c=labels, cmap='viridis', s=50)
plt.scatter(centroids[:, 0], centroids[:, 1], c='red', s=200, marker='X', label='Centroids')
plt.title("K-Means Clustering (Iris Dataset)")
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.legend()
plt.grid(True)
plt.show()