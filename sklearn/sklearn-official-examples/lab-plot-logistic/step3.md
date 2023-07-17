# Fit the classifier

After generating the dataset, we will fit the classifier using `LogisticRegression` from scikit-learn.

```python
# Fit the classifier
clf = LogisticRegression(C=1e5)
clf.fit(X, y)
```
