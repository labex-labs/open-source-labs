# 创建重叠的 theta 误差线

在这一步中，我们将创建重叠的 theta 误差线，以展示它们如何降低输出图形的可读性。

```python
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(projection='polar')
ax.errorbar(theta, r, xerr=5.25, yerr=0.1, capsize=7, fmt="o", c="darkred")
ax.set_title("Overlapping Theta Error Bars")
plt.show()
```
