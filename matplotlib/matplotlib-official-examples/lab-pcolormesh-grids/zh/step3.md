# 平面着色

Matplotlib 中的 `pcolormesh` 函数可以可视化二维网格。假设最少的网格规范是 `shading='flat'`，并且如果网格在每个维度上比数据大一个，即形状为 `(M+1, N+1)`。在这种情况下，`X` 和 `Y` 指定了用 `Z` 中的值进行着色的四边形的角。我们可以使用以下代码块来可视化该网格：

```python
fig, ax = plt.subplots()
ax.pcolormesh(X, Y, Z, shading='flat', cmap='viridis')
ax.set_title('Flat Shading')
plt.show()
```
