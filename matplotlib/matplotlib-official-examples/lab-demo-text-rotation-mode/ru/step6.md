# Выделяем ограничивающий прямоугольник текста

Если `rotation_mode` установлен в `'default'`, мы выделим ограничивающий прямоугольник текста с использованием прямоугольника. Мы будем использовать функцию `get_window_extent`, чтобы получить ограничивающий прямоугольник и преобразовать его в координаты данных с использованием атрибута `transData`.

```python
if mode == "default":
    fig.canvas.draw()
    for ax, text in texts.items():
        bb = text.get_window_extent().transformed(ax.transData.inverted())
        rect = plt.Rectangle((bb.x0, bb.y0), bb.width, bb.height,
                             facecolor="C1", alpha=0.3, zorder=2)
        ax.add_patch(rect)
```
