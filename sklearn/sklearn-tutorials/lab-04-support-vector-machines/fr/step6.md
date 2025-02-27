# Estimation de densité et détection de nouveauté

- Les SVM peuvent également être utilisés pour l'estimation de densité et la détection de nouveauté avec la classe `OneClassSVM` :

```python
clf = svm.OneClassSVM()
clf.fit(X)
clf.predict(X)
```
