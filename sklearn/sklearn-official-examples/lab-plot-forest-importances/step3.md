# Fit Random Forest

We will fit a random forest classifier to compute the feature importances.

```python
feature_names = [f"feature {i}" for i in range(X.shape[1])]
forest = RandomForestClassifier(random_state=0)
forest.fit(X_train, y_train)
```
