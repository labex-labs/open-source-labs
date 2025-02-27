# Charger et visualiser le jeu de données de chiffres

Nous allons charger le jeu de données de chiffres qui est composé d'images de 8x8 pixels de chiffres. Nous utiliserons la méthode `imshow()` de `matplotlib` pour visualiser les 4 premières images ainsi que leurs étiquettes correspondantes.

```python
digits = datasets.load_digits()

_, axes = plt.subplots(nrows=1, ncols=4, figsize=(10, 3))
for ax, image, label in zip(axes, digits.images, digits.target):
    ax.set_axis_off()
    ax.imshow(image, cmap=plt.cm.gray_r, interpolation="nearest")
    ax.set_title("Training: %i" % label)
```
