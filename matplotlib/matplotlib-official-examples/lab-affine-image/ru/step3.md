# Выполняем вращение изображения

В этом шаге мы выполняем вращение изображения с использованием функции `rotate_deg`. Мы передаем угол вращения в качестве входных данных в функцию `rotate_deg`. Мы используем функцию `do_plot` для отображения вращенного изображения.

```python
# prepare image and figure
fig, ax1 = plt.subplots()
Z = get_image()

# image rotation
do_plot(ax1, Z, mtransforms.Affine2D().rotate_deg(30))
```
