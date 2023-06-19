# Train the Regressors

Now, let's initiate a Gradient Boosting Regressor, a Random Forest Regressor, and a Linear Regression. Next, we will use the 3 regressors to build the Voting Regressor.

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
