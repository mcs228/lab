# Polynomial Regression Example (Using synthetic dataset)
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import mean_squared_error, r2_score

# Generate sample data
np.random.seed(42)
X = np.linspace(-5, 5, 30).reshape(-1, 1)
y = 2 * (X ** 2) + 3 * X + 5 + np.random.randn(30, 1) * 3 # Quadratic + noise

# Transform features to polynomial (degree = 2)
poly = PolynomialFeatures(degree=2)
X_poly = poly.fit_transform(X)

# Train Linear Regression on polynomial features
model = LinearRegression()
model.fit(X_poly, y)

# Predict
y_pred = model.predict(X_poly)

# Evaluate model
mse = mean_squared_error(y, y_pred)
r2 = r2_score(y, y_pred)

print("\n--- Polynomial Regression Model ---")
print(f"Equation: y = {model.intercept_[0]:.2f} + {model.coef_[0][1]:.2f}x + {model.coef_[0][2]:.2f}x²")
print(f"Mean Squared Error: {mse:.2f}")
print(f"R² Score: {r2:.2f}")

# Plot results
plt.scatter(X, y, color='blue', label="Actual Data")
plt.plot(X, y_pred, color='red', linewidth=2, label="Polynomial Fit (Degree 2)")
plt.title("Polynomial Regression (Degree 2)")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.show()