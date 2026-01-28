# Linear Discriminant Analysis (LDA) Example
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA

# Load dataset
iris = load_iris()
X = iris.data
y = iris.target
target_names = iris.target_names

# Standardize features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Apply LDA (reduce to 2 components for visualization)
lda = LDA(n_components=2)
X_lda = lda.fit_transform(X_scaled, y)

print("\n--- Linear Discriminant Analysis (LDA) ---")
print(f"Explained Variance Ratio: {lda.explained_variance_ratio_}")
print(f"Total Variance Captured: {sum(lda.explained variance ratio )*100:.2f}%")

# Plot the results
plt.figure(figsize=(8, 6))
colors = ['red', 'green', 'blue']
for color, i, target_name in zip(colors, [0, 1, 2], target_names):
    plt.scatter(X_lda[y == i, 0], X_lda[y == i, 1], color=color, label=target_name)

plt.title("LDA - Iris Dataset (2D Projection)")
plt.xlabel("Linear Discriminant 1")
plt.ylabel("Linear Discriminant 2")
plt.legend()
plt.grid(True)
plt.show()