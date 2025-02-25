# Обновляем изображения

Наконец, мы обновим изображения, чтобы они реагировали на изменения в нормировке других изображений. Это позволит нам изменить цветовую карту и цветовую шкалу одного изображения, и все остальные будут обновляться соответственно.

```python
def update(changed_image):
    for im in images:
        if (changed_image.get_cmap()!= im.get_cmap()
                or changed_image.get_clim()!= im.get_clim()):
            im.set_cmap(changed_image.get_cmap())
            im.set_clim(changed_image.get_clim())

for im in images:
    im.callbacks.connect('changed', update)
```
