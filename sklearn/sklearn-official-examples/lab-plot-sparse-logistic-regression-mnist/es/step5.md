# Evaluar el modelo

Evaluaremos el rendimiento del modelo calculando la esparsidad y la puntuación de precisión.

```python
esparsidad = np.mean(clf.coef_ == 0) * 100
puntuación = clf.score(X_test, y_test)

print("Esparsidad con penalización L1: %.2f%%" % esparsidad)
print("Puntuación de prueba con penalización L1: %.4f" % puntuación)
```
