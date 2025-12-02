import pandas as pd
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
import pickle
import json

# Load iris dataset
iris = load_iris()
X = iris.data
y = iris.target

# Train model
model = DecisionTreeClassifier()
model.fit(X, y)

# Save model
with open("iris.pkl", "wb") as f:
    pickle.dump(model, f)

# Save feature names + target names
data = {
    "feature_names": iris.feature_names,
    "target_names": iris.target_names.tolist()
}

with open("data.json", "w") as f:
    json.dump(data, f, indent=4)

print("Model retrained and saved!")

