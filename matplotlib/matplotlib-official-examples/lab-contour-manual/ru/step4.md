# Создаем заполненные контура с отверстиями

Множественные заполненные линии контура можно указать в одном списке вершин полигона вместе с списком типов вершин (типов кодов), как описано в классе Path. Это особенно полезно для полигона с отверстиями.

```python
fig, ax = plt.subplots()
filled01 = [[[0, 0], [3, 0], [3, 3], [0, 3], [1, 1], [1, 2], [2, 2], [2, 1]]]
M = Path.MOVETO
L = Path.LINETO
kinds01 = [[M, L, L, L, M, L, L, L]]
cs = ContourSet(ax, [0, 1], [filled01], [kinds01], filled=True)
cbar = fig.colorbar(cs)

ax.set(xlim=(-0.5, 3.5), ylim=(-0.5, 3.5),
       title='User specified filled contours with holes')
```
