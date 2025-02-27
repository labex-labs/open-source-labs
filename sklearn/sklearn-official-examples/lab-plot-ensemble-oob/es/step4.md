# Calcular la tasa de error OOB

Para cada clasificador, recorreremos un rango de valores de `n_estimators` y ajustaremos el clasificador al conjunto de datos. Registraremos la tasa de error OOB para cada valor de `n_estimators` y la almacenaremos en un objeto `OrderedDict`.

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
