# Problemas desequilibrados

- Las SVM pueden manejar problemas desequilibrados ajustando el parámetro `class_weight`:

```python
clf = svm.SVC(class_weight={1: 10})
clf.fit(X, y)
```
