# Ajustar el modelo con clases con pesos

Vamos a ajustar el modelo y obtener el hiperplano separador utilizando la función `SVC` de la biblioteca `svm`. Usaremos un kernel lineal y estableceremos `class_weight` en `{1: 10}`. Esto dará más peso a la clase más pequeña.

```python
wclf = svm.SVC(kernel="linear", class_weight={1: 10})
wclf.fit(X, y)
```
