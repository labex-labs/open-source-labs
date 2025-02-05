# Fit a Bagging Classifier

Now, we will fit a Bagging Classifier on the training data. The Bagging Classifier is an ensemble method that uses bootstrap sampling to create multiple base models (often decision trees) and aggregates their predictions using majority voting.

```python
bagging = BaggingClassifier(DecisionTreeClassifier(), n_estimators=10)
bagging.fit(X_train, y_train)
```
