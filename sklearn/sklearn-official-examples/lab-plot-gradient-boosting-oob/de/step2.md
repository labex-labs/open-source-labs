# Klassifizierer mit OOB-Schätzungen anpassen

Als nächstes erstellen wir einen Gradient Boosting Classifier mit OOB-Schätzungen mithilfe der Klasse `GradientBoostingClassifier` aus dem Modul `sklearn.ensemble`. Wir setzen die Anzahl der Schätzer auf 100 und die Lernrate auf 0,1.

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
