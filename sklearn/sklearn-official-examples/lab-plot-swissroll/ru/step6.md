# Визуализация набора данных Swiss-Hole

Можем визуализировать сгенерированный набор данных Swiss-Hole с использованием трехмерной точечной диаграммы, где разные цвета представляют разные точки.

```python
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection="3d")
fig.add_axes(ax)
ax.scatter(sh_points[:, 0], sh_points[:, 1], sh_points[:, 2], c=sh_color, s=50, alpha=0.8)
ax.set_title("Swiss-Hole в окружающем пространстве")
ax.view_init(azim=-66, elev=12)
_ = ax.text2D(0.8, 0.05, s="n_samples=1500", transform=ax.transAxes)
```
