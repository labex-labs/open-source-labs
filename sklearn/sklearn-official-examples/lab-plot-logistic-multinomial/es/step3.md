# Entrenar el modelo de regresión logística multinomial

Ahora entrenaremos un modelo de regresión logística multinomial usando la función `LogisticRegression` de scikit-learn. Estableceremos el resolvente en `"sag"`, el número máximo de iteraciones en 100, el estado aleatorio en 42 y la opción de multi-clase en `"multinomial"`. Luego imprimiremos la puntuación de entrenamiento del modelo.

```python
clf = LogisticRegression(
        solver="sag", max_iter=100, random_state=42, multi_class="multinomial"
    ).fit(X, y)

print("training score : %.3f (%s)" % (clf.score(X, y), "multinomial"))
```
