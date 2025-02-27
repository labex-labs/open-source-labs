# Ajustar el modelo

Vamos a ajustar el modelo y obtener el hiperplano separador utilizando la función `SVC` de la biblioteca `svm`. Usaremos un kernel lineal y estableceremos `C` en 1.0.

```python
clf = svm.SVC(kernel="linear", C=1.0)
clf.fit(X, y)
```
