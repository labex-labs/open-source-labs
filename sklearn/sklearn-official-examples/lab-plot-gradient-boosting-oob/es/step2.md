# Ajustar el clasificador con estimaciones OOB

A continuación, crearemos un clasificador de Gradient Boosting con estimaciones OOB utilizando la clase `GradientBoostingClassifier` del módulo `sklearn.ensemble`. Estableceremos el número de estimadores en 100 y la tasa de aprendizaje en 0.1.

```python
from sklearn.ensemble import GradientBoostingClassifier

params = {
    "n_estimators": 100,
    "learning_rate": 0.1,
    "subsample": 1.0,
    "max_depth": 3,
    "min_samples_leaf": 1,
    "random_state": 1,
    "oob_score": True
}

clf = GradientBoostingClassifier(**params)
clf.fit(X, y)
```
