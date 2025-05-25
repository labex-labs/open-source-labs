# Treinar os Regressores

Agora, vamos iniciar um Regressor de Reforço Gradiente, um Regressor de Floresta Aleatória e uma Regressão Linear. Em seguida, usaremos os 3 regressores para construir o Regressor de Votação.

```python
# Treinar classificadores
reg1 = GradientBoostingRegressor(random_state=1)
reg2 = RandomForestRegressor(random_state=1)
reg3 = LinearRegression()

reg1.fit(X, y)
reg2.fit(X, y)
reg3.fit(X, y)

ereg = VotingRegressor([("gb", reg1), ("rf", reg2), ("lr", reg3)])
ereg.fit(X, y)
```
