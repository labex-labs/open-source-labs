# Ajustar los modelos de regresión lineal

A continuación, ajustaremos tres modelos de regresión lineal utilizando los métodos de OLS, Theil-Sen y RANSAC.

```python
estimators = [
    ("OLS", LinearRegression()),
    ("Theil-Sen", TheilSenRegressor(random_state=42)),
    ("RANSAC", RANSACRegressor(random_state=42)),
]
colors = {"OLS": "turquesa", "Theil-Sen": "dorado", "RANSAC": "verde claro"}
lw = 2

line_x = np.array([-3, 3])
for name, estimator in estimators:
    t0 = time.time()
    estimator.fit(X, y)
    elapsed_time = time.time() - t0
    y_pred = estimator.predict(line_x.reshape(2, 1))
    plt.plot(
        line_x,
        y_pred,
        color=colors[name],
        linewidth=lw,
        label="%s (tiempo de ajuste: %.2fs)" % (name, elapsed_time),
    )
```
