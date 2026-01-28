# Support Vector Regression Example (SVR)
import numpy as np
import matplotlib.pyplot as plt
from sklearn.svm import SVR
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error, r2_score

# Generate synthetic data
np.random.seed(42)
X = np.sort(5 * np.random.rand(80, 1), axis=0)
y = np.sin(X).ravel() + np.random.randn(80) * 0.1 # Non-linear data

# Scale the data (important for SVR)
scaler_X = StandardScaler()
scaler_y = StandardScaler()
X_scaled = scaler_X.fit_transform(X)
y_scaled = scaler_y.fit_transform(y.reshape(-1, 1)).ravel()

# Train the SVR model
svr_rbf = SVR(kernel='rbf', C=100, gamma=0.1, epsilon=0.1)
svr_rbf.fit(X_scaled, y_scaled)

# Predict and inverse transform to original scale
y_pred_scaled = svr_rbf.predict(X_scaled)
y_pred = scaler_y.inverse_transform(y_pred_scaled.reshape(-1, 1))

# Evaluate performance
mse = mean_squared_error(y, y_pred)
r2 = r2_score(y, y_pred)
print("\n--- Support Vector Regression (RBF Kernel) ---")
print(f"Mean Squared Error: {mse:.3f}")
print(f"R² Score: {r2:.3f}")

# Plot results
plt.scatter(X, y, color='blue', label="Actual Data")
plt.plot(X, y_pred, color='red', lw=2, label="SVR (RBF Kernel)")
plt.title("Support Vector Regression (SVR) with RBF Kernel")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.show()