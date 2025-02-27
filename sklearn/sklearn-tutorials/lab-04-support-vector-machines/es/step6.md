# Estimación de densidad y detección de novedades

- Las SVM también se pueden utilizar para la estimación de densidad y la detección de novedades con la clase `OneClassSVM`:

```python
clf = svm.OneClassSVM()
clf.fit(X)
clf.predict(X)
```
