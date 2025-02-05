# 屏蔽数据点并创建散点图

我们根据数据点到原点的距离来屏蔽它们。距离小于 `r0` 的数据点在 `area1` 中被屏蔽，距离大于或等于 `r0` 的数据点在 `area2` 中被屏蔽。然后，我们分别为 `area1` 和 `area2` 创建一个带有 `marker='^'` 和 `marker='o'` 的屏蔽数据点的散点图。

```python
r = np.sqrt(x ** 2 + y ** 2)
area1 = np.ma.masked_where(r < r0, area)
area2 = np.ma.masked_where(r >= r0, area)
plt.scatter(x, y, s=area1, marker='^', c=c)
plt.scatter(x, y, s=area2, marker='o', c=c)
```
