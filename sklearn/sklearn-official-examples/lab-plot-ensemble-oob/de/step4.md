# Berechnen der OOB-Fehlerrate

Für jeden Klassifizierer werden wir durch einen Bereich von `n_estimators`-Werten iterieren und den Klassifizierer an den Datensatz anpassen. Wir werden die OOB-Fehlerrate für jeden `n_estimators`-Wert aufzeichnen und sie in einem `OrderedDict`-Objekt speichern.

```python
error_rate = OrderedDict((label, []) for label, _ in ensemble_clfs)

min_estimators = 15
max_estimators = 150

for label, clf in ensemble_clfs:
    for i in range(min_estimators, max_estimators + 1, 5):
        clf.set_params(n_estimators=i)
        clf.fit(X, y)

        oob_error = 1 - clf.oob_score_
        error_rate[label].append((i, oob_error))
```
