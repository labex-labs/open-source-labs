# Добавление цветовой шкалы

Добавьте цветовую шкалу на вставленную ось с помощью функции `inset_axes`. Задайте ширину, высоту, расположение и ограничивающий прямоугольник цветовой шкалы.

```python
cax = inset_axes(axins,
                 width="5%",  # width = 10% of parent_bbox width
                 height="100%",  # height : 50%
                 loc='lower left',
                 bbox_to_anchor=(1.05, 0., 1, 1),
                 bbox_transform=axins.transAxes,
                 borderpad=0,
                 )
fig.colorbar(im, cax=cax)
```
