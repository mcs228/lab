import math 
from collections import Counter

# --- Function to calculate Euclidean Distance ---
def euclidean_distance(p1, p2):
    distance = 0
    for i in range(len(p1)):
        distance += (p1[i] - p2[i]) ** 2
    return math.sqrt(distance)

# --- KNN Algorithm ---
def knn_classify(training_data, test_point, k):
    distances = []
    # Compute distances between test point and all training data
    
    for features, label in training_data:
        dist = euclidean_distance(features, test_point)
        distances.append((dist, label))
    
    # Sort by distance and take top-k
    distances.sort(key=lambda x: x[0])
    k_nearest = distances[:k]
    12# Find the majority class among k nearest neighbors
    k_labels = [label for _, label in k_nearest]
    prediction = Counter(k_labels).most_common(1)[0][0]
    return prediction

# --- MAIN PROGRAM ---
if __name__ == "__main__":
    # Sample training dataset: [features], label
    # Features: [weight, texture] | Texture: 1 = Smooth, 0 = Rough
    training_data = [
    ([150, 1], "Apple"),
    ([130, 0], "Orange"),
    ([160, 1], "Apple"),
    ([120, 0], "Orange"),
    ([155, 1], "Apple"),
    ]
    print("\n--- K-Nearest Neighbor (KNN) Algorithm ---")
    # Test input
    test_point = [140, 0] # Weight = 140g, Rough texture
    k = int(input("Enter the value of K: "))
    # Predict class
    result = knn_classify(training_data, test_point, k)
    print(f"\nTest Data: {test_point}")
    print(f"Predicted Class: {result}✅")