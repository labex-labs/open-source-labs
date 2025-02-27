# Обучение и предсказание с помощью Регурессоров дерева решений и AdaBoost

Теперь мы определяем классификаторы и настраиваем их на основе данных. Первый регрессор определяется как `DecisionTreeRegressor` с `max_depth=4`. Второй регрессор определяется как `AdaBoostRegressor` с `DecisionTreeRegressor` с `max_depth=4` в качестве базового обучателя. Мы создаем AdaBoost Regressor с `n_estimators=300` таких базовых обучателей. Затем мы настраиваем оба регрессора на основе данных и делаем предсказания на тех же данных, чтобы увидеть, насколько хорошо они подходят к ним.

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
