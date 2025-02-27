# Настройка оценщиков

Вторым шагом является настройка многорезультатных оценщиков на обучающих данных. Мы будем использовать четыре различных алгоритма: чрезвычайно случайные деревья, k-ближайших соседей, линейную регрессию и регрессию с ридж-регуляризацией. Оценщики будут предсказывать нижнюю часть лиц на основе верхней части.

```python
# Fit estimators
ESTIMATORS = {
    "Extra trees": ExtraTreesRegressor(
        n_estimators=10, max_features=32, random_state=0
    ),
    "K-nn": KNeighborsRegressor(),
    "Linear regression": LinearRegression(),
    "Ridge": RidgeCV(),
}

y_test_predict = dict()
for name, estimator in ESTIMATORS.items():
    estimator.fit(X_train, y_train)
    y_test_predict[name] = estimator.predict(X_test)
```
