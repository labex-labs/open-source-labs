# Загрузка и визуализация набора данных цифр

Мы загрузим набор данных цифр, состоящий из изображений цифр размером 8x8 пикселей. Мы будем использовать метод `imshow()` из `matplotlib` для визуализации первых 4 изображений вместе с их соответствующими метками.

```python
digits = datasets.load_digits()

_, axes = plt.subplots(nrows=1, ncols=4, figsize=(10, 3))
for ax, image, label in zip(axes, digits.images, digits.target):
    ax.set_axis_off()
    ax.imshow(image, cmap=plt.cm.gray_r, interpolation="nearest")
    ax.set_title("Training: %i" % label)
```
