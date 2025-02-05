# 创建较大半径的误差线

在这一步中，我们将创建较大半径的误差线，以展示它们如何导致数据中出现不必要的比例，从而缩小显示范围。

```python
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(projection='polar')
ax.errorbar(theta, r, xerr=0.25, yerr=10.1, capsize=7, fmt="o", c="orangered")
ax.set_title("Large Radius Error Bars")
plt.show()
```
