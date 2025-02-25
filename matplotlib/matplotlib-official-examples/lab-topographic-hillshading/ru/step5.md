# Создаем график

Мы создаем сетку графиков размером 4x3, чтобы показать карты с тенями холмов с разными режимами смешивания и вертикальной эксцентриситетом. Сначала показываем изображение интенсивности теней холмов в первой строке, а затем в остальных строках размещаем карты с тенями холмов с разными режимами смешивания. Мы используем цикл for для перебора различных значений вертикальной эксцентриситета и режимов смешивания.

```python
fig, axs = plt.subplots(nrows=4, ncols=3, figsize=(8, 9))
plt.setp(axs.flat, xticks=[], yticks=[])

for col, ve in zip(axs.T, [0.1, 1, 10]):
    col[0].imshow(ls.hillshade(z, vert_exag=ve, dx=dx, dy=dy), cmap='gray')
    for ax, mode in zip(col[1:], ['hsv', 'overlay','soft']):
        rgb = ls.shade(z, cmap=cmap, blend_mode=mode,
                       vert_exag=ve, dx=dx, dy=dy)
        ax.imshow(rgb)
```
