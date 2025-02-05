# 绘制直方图

既然我们已经计算出了绘图所需的量，就可以创建直方图了。我们将使用`barh`方法为每个直方图绘制水平条：

```python
# 所有直方图的箱边缘是相同的
bin_edges = np.linspace(hist_range[0], hist_range[1], number_of_bins + 1)
heights = np.diff(bin_edges)
centers = bin_edges[:-1] + heights / 2

# 循环并绘制每个直方图
fig, ax = plt.subplots()
for x_loc, binned_data in zip(x_locations, binned_data_sets):
    lefts = x_loc - 0.5 * binned_data
    ax.barh(centers, binned_data, height=heights, left=lefts)

ax.set_xticks(x_locations, labels)
ax.set_ylabel("数据值")
ax.set_xlabel("数据集")
```
