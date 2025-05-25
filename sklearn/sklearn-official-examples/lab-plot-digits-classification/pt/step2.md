# Carregar e Visualizar o Conjunto de Dados de Dígitos

Vamos carregar o conjunto de dados de dígitos, que consiste em imagens de dígitos de 8x8 pixels. Usaremos o método `imshow()` do `matplotlib` para visualizar as primeiras 4 imagens juntamente com as suas etiquetas correspondentes.

```python
digits = datasets.load_digits()

_, axes = plt.subplots(nrows=1, ncols=4, figsize=(10, 3))
for ax, image, label in zip(axes, digits.images, digits.target):
    ax.set_axis_off()
    ax.imshow(image, cmap=plt.cm.gray_r, interpolation="nearest")
    ax.set_title("Treino: %i" % label)
```
