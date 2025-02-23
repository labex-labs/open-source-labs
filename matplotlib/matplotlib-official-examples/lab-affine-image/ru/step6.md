# Выполняем несколько преобразований

В этом шаге мы выполняем несколько преобразований изображения с использованием функций `rotate_deg`, `skew_deg`, `scale` и `translate`. Мы передаем параметры преобразования в качестве входных данных в соответствующие функции. Мы используем функцию `do_plot` для отображения преобразованного изображения.

```python
# prepare image and figure
fig, ax4 = plt.subplots()
Z = get_image()

# everything and a translation
do_plot(ax4, Z, mtransforms.Affine2D().
        rotate_deg(30).skew_deg(30, 15).scale(-1,.5).translate(.5, -1))
```
