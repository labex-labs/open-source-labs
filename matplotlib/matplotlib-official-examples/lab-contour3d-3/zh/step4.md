# 将等高线轮廓投影到图形壁上

在这一步中，我们将通过为每个维度绘制具有适当偏移量的等高线，把等高线轮廓投影到图形壁上。

```python
# 绘制每个维度的等高线投影
ax.contour(X, Y, Z, zdir='z', offset=-100, cmap='coolwarm')
ax.contour(X, Y, Z, zdir='x', offset=-40, cmap='coolwarm')
ax.contour(X, Y, Z, zdir='y', offset=40, cmap='coolwarm')
```
