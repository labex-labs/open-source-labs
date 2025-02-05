# 平面着色，形状相同的网格

如果网格在每个维度上与数据的形状相同，我们就不能使用 `shading='flat'`。从历史上看，在这种情况下 Matplotlib 会默默地丢弃 `Z` 的最后一行和最后一列，以匹配 Matlab 的行为。如果仍然需要这种行为，只需手动丢弃最后一行和最后一列。我们可以使用以下代码块来可视化该网格：

```python
fig, ax = plt.subplots()
ax.pcolormesh(x, y, Z[:-1, :-1], shading='flat', cmap='viridis')
ax.set_title('Flat Shading, Same Shape Grid')
plt.show()
```
