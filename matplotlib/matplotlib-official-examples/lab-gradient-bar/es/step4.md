# Definir la función de barra de degradado

A continuación, necesitamos definir una función que creará una barra de degradado. Esta función tomará el objeto de ejes, las coordenadas x e y de la barra, el ancho de la barra y la posición inferior de la barra. Luego, la función creará una imagen de degradado para cada barra y la devolverá.

```python
def gradient_bar(ax, x, y, width=0.5, bottom=0):
    for left, top in zip(x, y):
        right = left + width
        gradient_image(ax, extent=(left, right, bottom, top),
                       cmap=plt.cm.Blues_r, cmap_range=(0, 0.8))
```
