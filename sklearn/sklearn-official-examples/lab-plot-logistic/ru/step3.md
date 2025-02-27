# Настроить классификатор

После генерации датасета мы настроим классификатор с использованием `LogisticRegression` из scikit-learn.

```python
# Fit the classifier
clf = LogisticRegression(C=1e5)
clf.fit(X, y)
```
