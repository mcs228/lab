# Support Vector Machine (SVM) for Data Classification
# Using Iris Dataset
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns

# Load the Iris dataset
iris = datasets.load_iris()
X = iris.data
y = iris.target

# Split dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Create and train the SVM model
model = SVC(kernel='rbf', gamma='auto')

# You can also try 'linear', 'poly', 'sigmoid'
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate performance
print("\n--- Support Vector Machine Classifier ---")
print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred, target_names=iris.target_names))

# Confusion Matrix
cm = confusion_matrix(y_test, y_pred)
plt.figure(figsize=(6, 4))
sns.heatmap(cm, annot=True, cmap="Greens", fmt='d',
    xticklabels=iris.target_names, yticklabels=iris.target_names)
plt.title("Confusion Matrix - SVM Classifier (Iris Dataset)")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.show()