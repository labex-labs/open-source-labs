# Definiendo la función de ejemplo de imagen y parche

Definimos la función `image_and_patch_example` que toma un objeto de eje como entrada, traza una imagen aleatoria y agrega un parche al trazado.

```python
def image_and_patch_example(ax):
    ax.imshow(np.random.random(size=(20, 20)), interpolation='none')
    c = plt.Circle((5, 5), radius=5, label='patch')
    ax.add_patch(c)
```
