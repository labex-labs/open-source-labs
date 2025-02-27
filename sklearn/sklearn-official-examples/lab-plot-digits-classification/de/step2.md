# Den Ziffern-Datensatz laden und visualisieren

Wir werden den Ziffern-Datensatz laden, der aus 8x8-Pixel-Bildern von Ziffern besteht. Wir werden die `imshow()`-Methode aus `matplotlib` verwenden, um die ersten 4 Bilder zusammen mit ihren zugehörigen Labels zu visualisieren.

```python
digits = datasets.load_digits()

_, axes = plt.subplots(nrows=1, ncols=4, figsize=(10, 3))
for ax, image, label in zip(axes, digits.images, digits.target):
    ax.set_axis_off()
    ax.imshow(image, cmap=plt.cm.gray_r, interpolation="nearest")
    ax.set_title("Training: %i" % label)
```
