# Вычисляем ошибку вне пакета (Out-Of-Bag, OOB)

Для каждого классификатора мы пройдем в цикле по диапазону значений `n_estimators` и подберем классификатор к набору данных. Мы запишем ошибку вне пакета для каждого значения `n_estimators` и сохраним ее в объекте `OrderedDict`.

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
