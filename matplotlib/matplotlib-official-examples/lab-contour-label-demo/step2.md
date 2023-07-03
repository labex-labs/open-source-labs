# Make contour labels with custom level formatters

We will now create contour labels with custom level formatters. This will allow us to format the labels in a specific way. In this case, we will remove trailing zeros and add a percent sign.

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
