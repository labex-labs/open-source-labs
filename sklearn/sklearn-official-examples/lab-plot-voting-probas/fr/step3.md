# Prédire les probabilités de classes pour tous les classifieurs

Nous allons prédire les probabilités de classes pour tous les classifieurs en utilisant la fonction predict_proba().

```python
probas = [c.fit(X, y).predict_proba(X) for c in (clf1, clf2, clf3, eclf)]
```
