# Crear clasificador SVM

En este paso, crearemos una instancia del clasificador SVM y ajustaremos nuestros datos. Usaremos el kernel personalizado creado en el paso anterior.

```python
clf = svm.SVC(kernel=my_kernel)
clf.fit(X, Y)
```
