# 使用自定义级别格式化器创建等高线标签

现在我们将使用自定义级别格式化器来创建等高线标签。这将使我们能够以特定方式格式化标签。在这种情况下，我们将去除末尾的零并添加百分号。

```python
def fmt(x):
    s = f"{x:.1f}"
    if s.endswith("0"):
        s = f"{x:.0f}"
    return rf"{s} \%" if plt.rcParams["text.usetex"] else f"{s} %"

fig, ax = plt.subplots()
CS = ax.contour(X, Y, Z)
ax.clabel(CS, CS.levels, inline=True, fmt=fmt, fontsize=10)
```
