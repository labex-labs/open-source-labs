# Выполняем сдвиг изображения

В этом шаге мы выполняем сдвиг изображения с использованием функции `skew_deg`. Мы передаем углы сдвига в качестве входных данных в функцию `skew_deg`. Мы используем функцию `do_plot` для отображения сдвинутого изображения.

```python
# prepare image and figure
fig, ax2 = plt.subplots()
Z = get_image()

# image skew
do_plot(ax2, Z, mtransforms.Affine2D().skew_deg(30, 15))
```
