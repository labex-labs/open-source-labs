# 在不同情况下演示稳健拟合

我们现在将使用四种不同的估计器：普通最小二乘法（OLS）、泰尔 - 森估计器（Theil - Sen）、随机抽样一致性算法（RANSAC）和稳健回归估计器（HuberRegressor），在不同情况下演示稳健拟合。

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
