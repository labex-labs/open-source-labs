# Drucken der besten Parameter und des Scores

Wir drucken die besten Parameter und den Score, die aus GridSearchCV erhalten wurden.

```python
print("Best parameter (CV score=%0.3f):" % search.best_score_)
print(search.best_params_)
```
