# Отображаем изображения в ImageGrid

Наконец, мы отображаем изображения в ImageGrid с использованием функции `imshow` и функции `zip`, чтобы перебирать оси в сетке.

```python
for ax, im in zip(grid, [im1, im2, im3]):
    ax.imshow(im, origin="lower", vmin=vmin, vmax=vmax)

plt.show()
```
