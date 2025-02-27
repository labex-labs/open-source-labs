# Присвоить метки наиболее неопределенным точкам

Мы добавим метки, введенные вручную, к помеченным точкам данных и обучим модель на них.

```python
y_train[uncertainty_index] = y[uncertainty_index]
lp_model.fit(X, y_train)
```
