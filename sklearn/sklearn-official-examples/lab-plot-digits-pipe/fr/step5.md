# Afficher les meilleurs paramètres et le score

Nous allons afficher les meilleurs paramètres et le score obtenus à partir de GridSearchCV.

```python
print("Meilleur paramètre (score CV = %0.3f) : " % search.best_score_)
print(search.best_params_)
```
