# Trainieren eines Entscheidungsbaum-Modells

In diesem Schritt trainieren wir ein Entscheidungsbaum-Modell auf dem ursprünglichen Datensatz.

```python
reg = DecisionTreeRegressor(min_samples_split=3, random_state=0).fit(X, y)
```
