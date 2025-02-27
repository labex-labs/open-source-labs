# Entrenar la máquina de vectores de soporte

Entrenaremos un clasificador de vectores de soporte en las muestras de entrenamiento utilizando el método `svm.SVC()` de `sklearn`.

```python
clf = svm.SVC(gamma=0.001)
clf.fit(X_train, y_train)
```
