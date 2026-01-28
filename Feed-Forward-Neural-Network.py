# Feed Forward Neural Network (FNN) for Classification
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report, accuracy_score

# Load dataset
data = load_breast_cancer()
X = data.data
y = data.target # 0 = malignant, 1 = benign

# Normalize features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, test_size=0.2, random_state=42
)

# Build the Feed Forward Neural Network
model = Sequential([
    Dense(16, input_dim=X_train.shape[1], activation='relu'), # Hidden Layer 1
    Dense(8, activation='relu'), # Hidden Layer 2
    Dense(1, activation='sigmoid') # Output Layer
])

# Compile the model
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Train the model
history = model.fit(X_train, y_train, epochs=100, batch_size=10, verbose=0)

# Evaluate on test set
loss, accuracy = model.evaluate(X_test, y_test, verbose=0)
print("\n--- Feed Forward Neural Network ---")
print(f"Test Accuracy: {accuracy * 100:.2f}%")

# Predict
y_pred = (model.predict(X_test) > 0.5).astype("int32")

print("\nClassification Report:")
print(classification_report(y_test, y_pred, target_names=data.target_names))