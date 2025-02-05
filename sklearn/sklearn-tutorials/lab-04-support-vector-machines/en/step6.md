# Density Estimation and Novelty Detection

- SVMs can also be used for density estimation and novelty detection with the `OneClassSVM` class:

```python
clf = svm.OneClassSVM()
clf.fit(X)
clf.predict(X)
```
