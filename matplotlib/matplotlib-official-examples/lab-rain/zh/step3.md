# 构建散点图

现在，我们将构建散点图，在动画过程中随着雨滴的变化对其进行更新。

```python
scat = ax.scatter(rain_drops['position'][:, 0], rain_drops['position'][:, 1],
                  s=rain_drops['size'], lw=0.5, edgecolors=rain_drops['color'],
                  facecolors='none')
```
