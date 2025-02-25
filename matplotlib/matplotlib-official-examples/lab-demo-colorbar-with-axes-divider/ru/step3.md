# Добавляем цветовую шкалу к графику

Теперь мы добавим цветовую шкалу к каждому подграфику с использованием функции `make_axes_locatable` из Matplotlib. Эта функция берет существующую ось, добавляет ее в новый `AxesDivider` и возвращает `AxesDivider`. Затем метод `append_axes` объекта `AxesDivider` можно использовать для создания новой оси по заданной стороне ("top", "right", "bottom" или "left") исходной оси.

```python
ax1_divider = make_axes_locatable(ax1)
cax1 = ax1_divider.append_axes("right", size="7%", pad="2%")
cb1 = fig.colorbar(im1, cax=cax1)

ax2_divider = make_axes_locatable(ax2)
cax2 = ax2_divider.append_axes("top", size="7%", pad="2%")
cb2 = fig.colorbar(im2, cax=cax2, orientation="horizontal")
cax2.xaxis.set_ticks_position("top")
```
