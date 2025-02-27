# Обучаем Ridge-регрессор

Теперь мы обучим Ridge-регрессор на наборе данных и сравним его производительность с производительностью HuberRegressor.

```python
# Fit a ridge regressor to compare it to huber regressor.
ridge = Ridge(alpha=0.0, random_state=0)
ridge.fit(X, y)
coef_ridge = ridge.coef_
coef_ = ridge.coef_ * x + ridge.intercept_
plt.plot(x, coef_, "g-", label="ridge regression")

# Add a legend to the plot
plt.legend(loc=0)

# Show the plot
plt.title("Comparison of HuberRegressor vs Ridge")
plt.xlabel("X")
plt.ylabel("y")
plt.show()
```
