# Training und Vorhersage mit DecisionTree und AdaBoost Regressoren

Wir definieren jetzt die Klassifizierer und trainieren sie mit den Daten. Wir definieren den ersten Regressor als `DecisionTreeRegressor` mit `max_depth=4`. Wir definieren den zweiten Regressor als `AdaBoostRegressor` mit einem `DecisionTreeRegressor` von `max_depth=4` als Basislehrer. Wir bauen den AdaBoost Regressor mit `n_estimators=300` dieser Basislehrer. Anschließend trainieren wir beide Regressoren mit den Daten und machen Vorhersagen auf den gleichen Daten, um zu sehen, wie gut sie die Daten approximieren.

```python
from sklearn.ensemble import AdaBoostRegressor
from sklearn.tree import DecisionTreeRegressor

regr_1 = DecisionTreeRegressor(max_depth=4)

regr_2 = AdaBoostRegressor(
    DecisionTreeRegressor(max_depth=4), n_estimators=300, random_state=rng
)

regr_1.fit(X, y)
regr_2.fit(X, y)

y_1 = regr_1.predict(X)
y_2 = regr_2.predict(X)
```
