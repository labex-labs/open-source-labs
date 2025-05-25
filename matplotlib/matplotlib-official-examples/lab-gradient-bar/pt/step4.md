# Definir a função de barra gradiente

Em seguida, precisamos definir uma função que criará uma barra gradiente. Esta função receberá o objeto de eixos (axes), as coordenadas x e y da barra, a largura da barra e a posição inferior da barra. A função então criará uma imagem gradiente para cada barra e a retornará.

```python
def gradient_bar(ax, x, y, width=0.5, bottom=0):
    for left, top in zip(x, y):
        right = left + width
        gradient_image(ax, extent=(left, right, bottom, top),
                       cmap=plt.cm.Blues_r, cmap_range=(0, 0.8))
```
