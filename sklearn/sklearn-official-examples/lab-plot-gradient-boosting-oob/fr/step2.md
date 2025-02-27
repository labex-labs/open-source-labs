# Ajuster le classifieur avec des estimations OOB

Ensuite, nous allons créer un classifieur Gradient Boosting avec des estimations OOB à l'aide de la classe `GradientBoostingClassifier` du module `sklearn.ensemble`. Nous définirons le nombre d'estimateurs sur 100 et le taux d'apprentissage sur 0,1.

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
