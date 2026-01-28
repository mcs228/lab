# Decision Tree Classifier Example (Using scikit-learn)

from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier, export_text, plot_tree
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt

# Load dataset
iris = load_iris()
X = iris.data
y = iris.target

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Create and train the Decision Tree model
clf = DecisionTreeClassifier(criterion="entropy", random_state=0)
clf.fit(X_train, y_train)

# Predict on test data
y_pred = clf.predict(X_test)

# Display results
print("\n--- Decision Tree Classifier ---")
print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nDecision Rules:\n")
print(export_text(clf, feature_names=iris.feature_names))

# Visualize the Decision Tree
plt.figure(figsize=(12, 8))
plot_tree(clf, feature_names=iris.feature_names, class_names=iris.target_names, filled=True)
plt.title("Decision Tree Visualization - Iris Dataset")
plt.show()