# Entrenar los regresores

Ahora, vamos a inicializar un Gradient Boosting Regressor, un Random Forest Regressor y una Linear Regression. A continuación, usaremos los 3 regresores para construir el Voting Regressor.

```python
# Entrenar clasificadores
reg1 = GradientBoostingRegressor(random_state=1)
reg2 = RandomForestRegressor(random_state=1)
reg3 = LinearRegression()

reg1.fit(X, y)
reg2.fit(X, y)
reg3.fit(X, y)

ereg = VotingRegressor([("gb", reg1), ("rf", reg2), ("lr", reg3)])
ereg.fit(X, y)
```
