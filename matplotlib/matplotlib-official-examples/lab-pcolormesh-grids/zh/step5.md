# 最近点着色，形状相同的网格

通常情况下，当用户使 `X`、`Y` 和 `Z` 具有相同形状时，他们并不是想丢弃一行和一列数据。对于这种情况，Matplotlib 允许使用 `shading='nearest'`，并将着色的四边形以网格点为中心。如果传递了形状不正确的网格并使用 `shading='nearest'`，则会引发错误。我们可以使用以下代码块来可视化该网格：

```python
fig, ax = plt.subplots()
ax.pcolormesh(X, Y, Z, shading='nearest', cmap='viridis')
ax.set_title('Nearest Shading, Same Shape Grid')
plt.show()
```
