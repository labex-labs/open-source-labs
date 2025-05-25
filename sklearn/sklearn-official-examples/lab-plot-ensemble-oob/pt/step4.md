# Calcular a Taxa de Erro OOB

Para cada classificador, percorreremos um intervalo de valores de `n_estimators` e ajustaremos o classificador ao conjunto de dados. Registraremos a taxa de erro OOB para cada valor de `n_estimators` e a armazenaremos em um objeto `OrderedDict`.

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
