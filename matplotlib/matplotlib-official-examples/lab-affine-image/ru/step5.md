# Выполняем масштабирование и отражение изображения

В этом шаге мы выполняем масштабирование и отражение изображения с использованием функции `scale`. Мы передаем коэффициенты масштабирования и отражения в качестве входных данных в функцию `scale`. Мы используем функцию `do_plot` для отображения масштабированного и отраженного изображения.

```python
# prepare image and figure
fig, ax3 = plt.subplots()
Z = get_image()

# scale and reflection
do_plot(ax3, Z, mtransforms.Affine2D().scale(-1,.5))
```
