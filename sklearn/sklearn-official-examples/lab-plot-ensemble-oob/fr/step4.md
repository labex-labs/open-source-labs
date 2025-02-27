# Calculer le taux d'erreur hors-bag (OOB)

Pour chaque classifieur, nous allons parcourir une plage de valeurs de `n_estimators` et ajuster le classifieur à l'ensemble de données. Nous allons enregistrer le taux d'erreur hors-bag pour chaque valeur de `n_estimators` et le stocker dans un objet `OrderedDict`.

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
