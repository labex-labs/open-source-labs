# 回帰係数を比較する

ここでは、非負最小二乗回帰と古典的な線形回帰の間の回帰係数を比較します。係数同士をプロットし、それらが高度に相関していることを観察します。ただし、非負制約により、一部の係数が0に収束します。これは、非負最小二乗が本質的に疎な結果をもたらすためです。

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
