# Entrenar el modelo

En este paso, entrenaremos el clasificador SVM con un kernel RBF utilizando los datos generados.

```python
clf = svm.NuSVC(gamma="auto")
clf.fit(X, Y)
```
