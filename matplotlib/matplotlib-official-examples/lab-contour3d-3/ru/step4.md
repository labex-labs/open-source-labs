# Проецируем профили контуров на стены графика

В этом шаге мы проецируем профили контуров на стены графика, построив контуры для каждой размерности с соответствующими смещениями.

```python
# Plot projections of the contours for each dimension
ax.contour(X, Y, Z, zdir='z', offset=-100, cmap='coolwarm')
ax.contour(X, Y, Z, zdir='x', offset=-40, cmap='coolwarm')
ax.contour(X, Y, Z, zdir='y', offset=40, cmap='coolwarm')
```
