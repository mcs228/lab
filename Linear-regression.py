# Linear Regression Example using Boston Housing Dataset
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_diabetes
# Using diabetes dataset (Boston is deprecated)
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Load dataset
data = load_diabetes()
X = data.data
y = data.target

# Select one feature for easy visualization (e.g., BMI)
X = X[:, np.newaxis, 2]

# Split into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and train model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("\n--- Linear Regression Model ---")
print("Coefficient (Slope):", model.coef_[0])
print("Intercept:", model.intercept_)
print(f"Mean Squared Error: {mse:.2f}")
print(f"R² Score: {r2:.2f}")

# Visualization
plt.scatter(X_test, y_test, color='blue', label="Actual Data")
plt.plot(X_test, y_pred, color='red', linewidth=2, label="Regression Line")
plt.xlabel("BMI")
plt.ylabel("Disease Progression")
plt.title("Linear Regression - Diabetes Dataset")
plt.legend()
plt.show()