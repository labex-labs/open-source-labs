# Обучение регрессоров

Теперь инициализируем Регурессор градиентного бустинга, Случайный лес регрессор и Линейную регрессию. Затем будем использовать эти 3 регрессора для построения Регурессора голосования.

```python
# Train classifiers
reg1 = GradientBoostingRegressor(random_state=1)
reg2 = RandomForestRegressor(random_state=1)
reg3 = LinearRegression()

reg1.fit(X, y)
reg2.fit(X, y)
reg3.fit(X, y)

ereg = VotingRegressor([("gb", reg1), ("rf", reg2), ("lr", reg3)])
ereg.fit(X, y)
```
