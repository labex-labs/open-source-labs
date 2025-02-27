# Passt den Ridge-Regressor an

Wir werden nun den Ridge-Regressor an den Datensatz anpassen und dessen Leistung mit der des HuberRegressors vergleichen.

```python
# Passt einen Ridge-Regressor an, um ihn mit dem Huber-Regressor zu vergleichen.
ridge = Ridge(alpha=0.0, random_state=0)
ridge.fit(X, y)
coef_ridge = ridge.coef_
coef_ = ridge.coef_ * x + ridge.intercept_
plt.plot(x, coef_, "g-", label="ridge regression")

# Füge eine Legende zum Plot hinzu
plt.legend(loc=0)

# Zeige den Plot an
plt.title("Vergleich von HuberRegressor und Ridge")
plt.xlabel("X")
plt.ylabel("y")
plt.show()
```
