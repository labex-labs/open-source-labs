# Predecir las probabilidades de clase para todos los clasificadores

Predeciremos las probabilidades de clase para todos los clasificadores utilizando la función predict_proba().

```python
probas = [c.fit(X, y).predict_proba(X) for c in (clf1, clf2, clf3, eclf)]
```
