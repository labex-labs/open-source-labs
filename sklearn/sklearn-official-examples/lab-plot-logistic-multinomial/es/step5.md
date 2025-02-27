# Entrenar el modelo de regresión logística one-vs-rest

Ahora entrenaremos un modelo de regresión logística one-vs-rest usando los mismos parámetros que en el Paso 3, pero con la opción de multi-clase establecida en `"ovr"`. Luego imprimiremos la puntuación de entrenamiento del modelo.

```python
clf = LogisticRegression(
        solver="sag", max_iter=100, random_state=42, multi_class="ovr"
    ).fit(X, y)

print("training score : %.3f (%s)" % (clf.score(X, y), "ovr"))
```
