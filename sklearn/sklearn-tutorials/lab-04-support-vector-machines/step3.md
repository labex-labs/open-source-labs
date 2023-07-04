# Scores and Probabilities

- SVMs do not directly provide probability estimates, but you can enable probability estimation by setting the `probability` parameter to `True`:

```python
clf = svm.SVC(probability=True)
clf.fit(X, y)
```

- You can then use the `predict_proba` method to get the probabilities of each class:

```python
clf.predict_proba([[2., 2.]])
```

- Note that probability estimation is expensive and requires cross-validation, so use it judiciously.
