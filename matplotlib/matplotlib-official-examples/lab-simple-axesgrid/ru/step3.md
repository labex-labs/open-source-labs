# Перебираем сетку и отображаем изображения

Затем мы перебираем объект `grid` с использованием функции `zip`, чтобы перебрать как оси, так и массивы изображений. Мы отображаем каждое изображение на соответствующей оси с использованием функции `imshow`.

```python
for ax, im in zip(grid, [im1, im2, im3, im4]):
    ax.imshow(im)
```
