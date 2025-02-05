# 比较回归系数

现在我们将比较非负最小二乘回归和经典线性回归之间的回归系数。我们将把这些系数相互绘制出来，并观察到它们高度相关。然而，非负约束会将一些系数缩减为 0。这是因为非负最小二乘本质上会产生稀疏结果。

```python
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.plot(reg_ols.coef_, reg_nnls.coef_, linewidth=0, marker=".")

low_x, high_x = ax.get_xlim()
low_y, high_y = ax.get_ylim()
low = max(low_x, low_y)
high = min(high_x, high_y)
ax.plot([low, high], [low, high], ls="--", c=".3", alpha=0.5)
ax.set_xlabel("OLS regression coefficients", fontweight="bold")
ax.set_ylabel("NNLS regression coefficients", fontweight="bold")
```
