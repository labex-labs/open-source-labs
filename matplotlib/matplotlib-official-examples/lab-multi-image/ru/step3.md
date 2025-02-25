# Настраиваем цветовую шкалу и создаем цветовую шкалу (colorbar)

Теперь мы настроим цветовую шкалу для наших изображений и создадим цветовую шкалу, чтобы показать диапазон значений. Мы найдем минимальные и максимальные значения для всех изображений и нормализуем цветовую шкалу соответственно.

```python
vmin = min(image.get_array().min() for image in images)
vmax = max(image.get_array().max() for image in images)
norm = colors.Normalize(vmin=vmin, vmax=vmax)
for im in images:
    im.set_norm(norm)

fig.colorbar(images[0], ax=axs, orientation='horizontal', fraction=.1)
```
