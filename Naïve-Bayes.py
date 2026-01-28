from collections import defaultdict, Counter


class NaiveBayesClassifier:
    def __init__(self):
        self.class_probs = {}  # P(C)
        self.feature_probs = {}  # P(X|C)

    def train(self, data, labels):
        total_samples = len(data)
        label_counts = Counter(labels)

        # Calculate prior probabilities P(C)
        self.class_probs = {
            label: count / total_samples for label, count in label_counts.items()
        }

        # Calculate conditional probabilities P(X|C)
        feature_counts = defaultdict(lambda: defaultdict(lambda: Counter()))
        for features, label in zip(data, labels):
            for feature_name, feature_value in features.items():
                feature_counts[label][feature_name][feature_value] += 1

        self.feature_probs = {
            label: {
                feature: {
                    value: count / label_counts[label]
                    for value, count in feature_values.items()
                }
                for feature, feature_values in features.items()
            }
            for label, features in feature_counts.items()
        }

    def predict(self, input_features):
        results = {}

        for label in self.class_probs:
            prob = self.class_probs[label]
            for feature_name, feature_value in input_features.items():
                prob *= (
                    self.feature_probs[label]
                    .get(feature_name, {})
                    .get(feature_value, 1e-6)
                )
            results[label] = prob
        return max(results, key=results.get)


# --- MAIN PROGRAM ---
if __name__ == "__main__":
    # Dataset
    data = [
        {"Outlook": "Sunny", "Temperature": "Hot", "Humidity": "High", "Windy": False},
        {"Outlook": "Sunny", "Temperature": "Hot", "Humidity": "High", "Windy": True},
        {
            "Outlook": "Overcast",
            "Temperature": "Hot",
            "Humidity": "High",
            "Windy": False,
        },
        {"Outlook": "Rain", "Temperature": "Mild", "Humidity": "High", "Windy": False},
        {
            "Outlook": "Rain",
            "Temperature": "Cool",
            "Humidity": "Normal",
            "Windy": False,
        },
        {"Outlook": "Rain", "Temperature": "Cool", "Humidity": "Normal", "Windy": True},
        {
            "Outlook": "Overcast",
            "Temperature": "Cool",
            "Humidity": "Normal",
            "Windy": True,
        },
        {"Outlook": "Sunny", "Temperature": "Mild", "Humidity": "High", "Windy": False},
        {
            "Outlook": "Sunny",
            "Temperature": "Cool",
            "Humidity": "Normal",
            "Windy": False,
        },
        {
            "Outlook": "Rain",
            "Temperature": "Mild",
            "Humidity": "Normal",
            "Windy": False,
        },
        {
            "Outlook": "Sunny",
            "Temperature": "Mild",
            "Humidity": "Normal",
            "Windy": True,
        },
        {
            "Outlook": "Overcast",
            "Temperature": "Mild",
            "Humidity": "High",
            "Windy": True,
        },
        {
            "Outlook": "Overcast",
            "Temperature": "Hot",
            "Humidity": "Normal",
            "Windy": False,
        },
        {"Outlook": "Rain", "Temperature": "Mild", "Humidity": "High", "Windy": True},
    ]
    labels = [
        "No",
        "No",
        "Yes",
        "Yes",
        "Yes",
        "No",
        "Yes",
        "No",
        "Yes",
        "Yes",
        "Yes",
        "Yes",
        "Yes",
        "No",
    ]
    # Train model
    nb = NaiveBayesClassifier()
    nb.train(data, labels)
    # Test case
    test_sample = {
        "Outlook": "Sunny",
        "Temperature": "Cool",
        "Humidity": "High",
        "Windy": True,
    }
    prediction = nb.predict(test_sample)
    print("\n--- Naïve Bayes Classifier ---")
    print(f"Test Sample: {test_sample}")
    print(f"Predicted Class: {prediction} ✅")
