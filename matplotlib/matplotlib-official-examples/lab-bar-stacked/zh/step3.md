# 创建堆叠柱状图

我们将使用 `matplotlib.pyplot.bar` 创建一个堆叠柱状图，并遍历每个体重类别以堆叠这些柱子。

```python
fig, ax = plt.subplots()
bottom = np.zeros(3)

for boolean, weight_count in weight_counts.items():
    p = ax.bar(species, weight_count, width, label=boolean, bottom=bottom)
    bottom += weight_count

ax.set_title("体重高于平均水平的企鹅数量")
ax.legend(loc="upper right")
```
