# Trainieren eines Entscheidungsbaum-Modells auf dem diskretisierten Datensatz

In diesem Schritt trainieren wir ein Entscheidungsbaum-Modell auf dem diskretisierten Datensatz.

```python
reg = DecisionTreeRegressor(min_samples_split=3, random_state=0).fit(X_binned, y)
```
