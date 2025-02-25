# 大きな半径の誤差棒を作成する

このステップでは、データに不要なスケールを引き起こし、表示範囲を狭める方法を示すために、大きな半径の誤差棒を作成します。

```python
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(projection='polar')
ax.errorbar(theta, r, xerr=0.25, yerr=10.1, capsize=7, fmt="o", c="orangered")
ax.set_title("Large Radius Error Bars")
plt.show()
```
