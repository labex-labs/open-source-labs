# Cargar y visualizar el conjunto de datos de dígitos

Cargaremos el conjunto de datos de dígitos que consta de imágenes de dígitos de 8x8 píxeles. Utilizaremos el método `imshow()` de `matplotlib` para visualizar las primeras 4 imágenes junto con sus correspondientes etiquetas.

```python
digits = datasets.load_digits()

_, axes = plt.subplots(nrows=1, ncols=4, figsize=(10, 3))
for ax, image, label in zip(axes, digits.images, digits.target):
    ax.set_axis_off()
    ax.imshow(image, cmap=plt.cm.gray_r, interpolation="nearest")
    ax.set_title("Training: %i" % label)
```
