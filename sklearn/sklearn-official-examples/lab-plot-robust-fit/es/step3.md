# Demostrar el ajuste robusto en diferentes situaciones

Ahora demostraremos el ajuste robusto en diferentes situaciones utilizando cuatro estimadores diferentes: OLS, Theil-Sen, RANSAC y HuberRegressor.

```python
estimators = [
    ("OLS", LinearRegression()),
    ("Theil-Sen", TheilSenRegressor(random_state=42)),
    ("RANSAC", RANSACRegressor(random_state=42)),
    ("HuberRegressor", HuberRegressor()),
]
colors = {
    "OLS": "turquesa",
    "Theil-Sen": "dorado",
    "RANSAC": "verde claro",
    "HuberRegressor": "negro",
}
linestyle = {"OLS": "-", "Theil-Sen": "-.", "RANSAC": "--", "HuberRegressor": "--"}
lw = 3
```
