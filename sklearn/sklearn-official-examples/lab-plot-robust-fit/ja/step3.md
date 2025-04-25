# さまざまな状況での堅牢なフィッティングのデモ

ここでは、4 つの異なる推定器（OLS、Theil - Sen、RANSAC、および HuberRegressor）を使って、さまざまな状況での堅牢なフィッティングをデモします。

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
