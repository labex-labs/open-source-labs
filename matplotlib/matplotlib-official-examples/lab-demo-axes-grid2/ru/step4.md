# Демонстрация 1 - Цветовая шкала для каждой оси

Мы создадим сетку из 3 изображений с цветовой шкалой для каждой оси с использованием следующего кода:

```python
grid = ImageGrid(
    fig, 211, nrows_ncols=(1, 3), axes_pad=0.05, label_mode="1", share_all=True,
    cbar_location="top", cbar_mode="each", cbar_size="7%", cbar_pad="1%")
grid[0].set(xticks=[-2, 0], yticks=[-2, 0, 2])

for i, (ax, z) in enumerate(zip(grid, ZS)):
    im = ax.imshow(z, origin="lower", extent=extent)
    cb = ax.cax.colorbar(im)
    # Changing the colorbar ticks
    if i in [1, 2]:
        cb.set_ticks([-1, 0, 1])

for ax, im_title in zip(grid, ["Image 1", "Image 2", "Image 3"]):
    add_inner_title(ax, im_title, loc='lower left')
```

- Мы создаем сетку из 3 изображений с использованием `ImageGrid`.
- Мы устанавливаем `cbar_mode` в "each", чтобы добавить цветовую шкалу для каждой оси.
- Мы устанавливаем параметр `share_all` в True, чтобы совместить оси x и y для всех изображений.
- Мы устанавливаем параметр `cbar_location` в "top", чтобы расположить цветовые шкалы вверху.
- Мы задаем `xticks` и `yticks` для первого изображения.
- Мы перебираем каждое изображение и добавляем его на ось с использованием `imshow`.
- Мы добавляем цветовую шкалу для каждой оси с использованием `ax.cax.colorbar`.
- Мы задаем деления цветовой шкалы для второго и третьего изображений.
- Мы добавляем заголовок к каждому изображению с использованием `add_inner_title`.
