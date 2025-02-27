# Definieren des Parameterspaces

Definiere ein Dictionary `param_dist`, das die Hyperparameter und ihre jeweiligen Werte enthält, durch die gesucht werden soll. Die Hyperparameter sind `max_depth`, `max_features`, `min_samples_split`, `bootstrap` und `criterion`. Der Suchbereich für `max_features` und `min_samples_split` wird mit der Funktion `randint` aus dem Modul `scipy.stats` definiert. Der Code zum Definieren des Parameterspaces lautet wie folgt:

```python
param_dist = {
    "max_depth": [3, None],
    "max_features": randint(1, 6),
    "min_samples_split": randint(2, 11),
    "bootstrap": [True, False],
    "criterion": ["gini", "entropy"],
}
```
