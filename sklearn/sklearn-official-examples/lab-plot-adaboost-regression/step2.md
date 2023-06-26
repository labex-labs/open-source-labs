# Training and prediction with DecisionTree and AdaBoost Regressors

We now define the classifiers and fit them to the data. We define the first regressor as a `DecisionTreeRegressor` with `max_depth=4`. We define the second regressor as an `AdaBoostRegressor` with a `DecisionTreeRegressor` of `max_depth=4` as base learner. We build the AdaBoost Regressor with `n_estimators=300` of those base learners. We then fit both regressors to the data and make predictions on the same data to see how well they fit it.

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
