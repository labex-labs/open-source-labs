# 誤差棒を作成する

このステップでは、極座標軸上に誤差棒を作成します。半径方向と theta 方向の誤差棒を作成するために、`errorbar()`関数を使用します。

```python
ax.errorbar(theta, r, xerr=0.25, yerr=0.1, capsize=7, fmt="o", c="seagreen")
```
