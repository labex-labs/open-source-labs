# Демонстрация 2 - Общая цветовая шкала

Мы создадим сетку из 3 изображений с общей цветовой шкалой с использованием следующего кода:

```python
grid2 = ImageGrid(
    fig, 212, nrows_ncols=(1, 3), axes_pad=0.05, label_mode="1", share_all=True,
    cbar_location="right", cbar_mode="single", cbar_size="10%", cbar_pad=0.05)
grid2[0].set(xlabel="X", ylabel="Y", xticks=[-2, 0], yticks=[-2, 0, 2])

clim = (np.min(ZS), np.max(ZS))
for ax, z in zip(grid2, ZS):
    im = ax.imshow(z, clim=clim, origin="lower", extent=extent)

# With cbar_mode="single", cax attribute of all axes are identical.
ax.cax.colorbar(im)

for ax, im_title in zip(grid2, ["(a)", "(b)", "(c)"]):
    add_inner_title(ax, im_title, loc='upper left')
```

- Мы создаем сетку из 3 изображений с использованием `ImageGrid`.
- Мы устанавливаем `cbar_mode` в "single", чтобы добавить общую цветовую шкалу.
- Мы устанавливаем параметр `share_all` в True, чтобы совместить оси x и y для всех изображений.
- Мы устанавливаем параметр `cbar_location` в "right", чтобы расположить цветовую шкалу справа.
- Мы задаем `xticks` и `yticks` для первого изображения.
- Мы перебираем каждое изображение и добавляем его на ось с использованием `imshow`.
- Мы устанавливаем параметр `clim`, чтобы убедиться, что все изображения используют одинаковую цветовую шкалу.
- Мы добавляем общую цветовую шкалу на ось с использованием `ax.cax.colorbar`.
- Мы добавляем заголовок к каждому изображению с использованием `add_inner_title`.
