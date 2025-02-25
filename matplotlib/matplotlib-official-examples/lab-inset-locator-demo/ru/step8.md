# Создание вставки, центрированной в координатах рисунка

Мы можем создать вставку, которая по горизонтали центрирована в координатах рисунка и по вертикали привязана к выравниванию с осями, используя метод `blended_transform_factory()`, чтобы создать смешанное преобразование и используя его в качестве параметра `bbox_transform`.

```python
# Создайте вставку, которая по горизонтали центрирована в координатах рисунка и по вертикали
# привязана к выравниванию с осями.
from matplotlib.transforms import blended_transform_factory

transform = blended_transform_factory(fig.transFigure, ax2.transAxes)
axins4 = inset_axes(ax2, width="16%", height="34%",
                    bbox_to_anchor=(0, 0, 1, 1),
                    bbox_transform=transform, loc=8, borderpad=0)
```
