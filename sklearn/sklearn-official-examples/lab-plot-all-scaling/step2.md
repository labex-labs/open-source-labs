# Select Features and Define Feature Mapping

Next, we select two features from the dataset to make visualization easier and define a mapping of the feature names for better visualization.

```python
# Select two features
features = ["MedInc", "AveOccup"]
features_idx = [feature_names.index(feature) for feature in features]
X = X_full[:, features_idx]

# Define feature mapping
feature_mapping = {
    "MedInc": "Median income in block",
    "AveOccup": "Average house occupancy",
}
```
