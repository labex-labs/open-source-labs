# Entraîner les régresseurs

Maintenant, initialisons un Gradient Boosting Regressor, un Random Forest Regressor et une Régression Linéaire. Ensuite, nous utiliserons les 3 régresseurs pour construire le Voting Regressor.

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
