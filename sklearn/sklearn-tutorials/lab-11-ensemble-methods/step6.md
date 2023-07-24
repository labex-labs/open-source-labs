# Fit a Random Forest Classifier

Next, we will fit a Random Forest Classifier on the training data. The Random Forest Classifier is also an ensemble method that uses bootstrap sampling to create multiple decision trees, but it also adds additional randomness by considering only a subset of features at each split.

```python
random_forest = RandomForestClassifier(n_estimators=10)
random_forest.fit(X_train, y_train)
```
