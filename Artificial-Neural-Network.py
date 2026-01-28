# Artificial Neural Network for Classification (Iris Dataset)
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelBinarizer
from sklearn.metrics import classification_report, accuracy_score

# Load dataset
iris = load_iris()
X = iris.data
y = iris.target

# Normalize data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# One-hot encode target labels
lb = LabelBinarizer()
y_encoded = lb.fit_transform(y)

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y_encoded, test_size=0.2, random_state=42
)

# Build the ANN model
model = Sequential([
    Dense(10, input_dim=4, activation='relu'), # Hidden layer 1
    Dense(8, activation='relu'), # Hidden layer 2
    Dense(3, activation='softmax') # Output layer (3 classes)
])

# Compile model
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Train model
history = model.fit(X_train, y_train, epochs=100, batch_size=8, verbose=0)

# Evaluate
loss, accuracy = model.evaluate(X_test, y_test, verbose=0)
print("\n--- Artificial Neural Network Classification ---")
print(f"Test Accuracy: {accuracy * 100:.2f}%")

# Predictions
y_pred = model.predict(X_test)
y_pred_classes = np.argmax(y_pred, axis=1)
y_true_classes = np.argmax(y_test, axis=1)

print("\nClassification Report:")
print(classification_report(y_true_classes, y_pred_classes, target_names=iris.target_names))