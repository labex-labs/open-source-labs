# Evaluar el flujo de trabajo

En este paso, evaluaremos el rendimiento de nuestro flujo de trabajo calculando la puntuación del modelo.

```python
print("model score: %.3f" % clf.score(X_test, y_test))
```
