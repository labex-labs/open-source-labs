# Trainieren der Regressoren

Lassen Sie uns nun einen Gradient Boosting Regressor, einen Random Forest Regressor und eine Lineare Regression initialisieren. Anschließend werden wir die 3 Regressoren verwenden, um den Voting Regressor zu erstellen.

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
