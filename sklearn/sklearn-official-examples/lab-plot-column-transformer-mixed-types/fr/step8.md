# Évaluer le pipeline

Dans cette étape, nous allons évaluer les performances de notre pipeline en calculant le score du modèle.

```python
print("model score: %.3f" % clf.score(X_test, y_test))
```
