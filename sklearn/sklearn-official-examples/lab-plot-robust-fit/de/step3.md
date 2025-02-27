# Demonstrieren der robusten Anpassung in verschiedenen Situationen

Wir werden nun die robuste Anpassung in verschiedenen Situationen mit vier verschiedenen Schätzern demonstrieren: OLS, Theil-Sen, RANSAC und HuberRegressor.

```python
estimators = [
    ("OLS", LinearRegression()),
    ("Theil-Sen", TheilSenRegressor(random_state=42)),
    ("RANSAC", RANSACRegressor(random_state=42)),
    ("HuberRegressor", HuberRegressor()),
]
colors = {
    "OLS": "turquoise",
    "Theil-Sen": "gold",
    "RANSAC": "lightgreen",
    "HuberRegressor": "black",
}
linestyle = {"OLS": "-", "Theil-Sen": "-.", "RANSAC": "--", "HuberRegressor": "--"}
lw = 3
```
