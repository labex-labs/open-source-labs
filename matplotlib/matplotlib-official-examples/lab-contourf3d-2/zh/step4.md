# 绘制三维表面

我们将使用 `plot_surface` 方法绘制三维表面。我们还将设置一些参数，如边缘颜色、线宽和透明度。

```python
ax.plot_surface(X, Y, Z, edgecolor='royalblue', lw=0.5, rstride=8, cstride=8, alpha=0.3)
```
