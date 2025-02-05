# 高洛德着色

也可以指定 `高洛德着色`，其中四边形内的颜色在网格点之间进行线性插值。`X`、`Y`、`Z` 的形状必须相同。我们可以使用以下代码块来可视化该网格：

```python
fig, ax = plt.subplots()
ax.pcolormesh(X, Y, Z, shading='gouraud', cmap='viridis')
ax.set_title('Gouraud Shading')
plt.show()
```
