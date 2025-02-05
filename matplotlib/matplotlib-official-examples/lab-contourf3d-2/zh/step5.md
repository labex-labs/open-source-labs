# 投影等高线轮廓

现在我们将把等高线轮廓投影到图形的壁面上。这通过 `contourf` 方法来完成。我们将把 `zdir` 参数设置为 'z'、'x' 和 'y'，以便分别将等高线轮廓投影到 z、x 和 y 壁面上。我们还将设置 `offset` 参数以匹配适当的坐标轴范围。

```python
ax.contourf(X, Y, Z, zdir='z', offset=-100, cmap='coolwarm')
ax.contourf(X, Y, Z, zdir='x', offset=-40, cmap='coolwarm')
ax.contourf(X, Y, Z, zdir='y', offset=40, cmap='coolwarm')
```
