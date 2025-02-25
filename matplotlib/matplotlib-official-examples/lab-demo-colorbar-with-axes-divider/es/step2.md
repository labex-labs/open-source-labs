# Crear una gráfica

A continuación, crearemos una gráfica utilizando la función `imshow` de Matplotlib. Esta función muestra una imagen en la gráfica. También crearemos una figura con dos subgráficos.

```python
fig, (ax1, ax2) = plt.subplots(1, 2)
fig.subplots_adjust(wspace=0.5)

im1 = ax1.imshow([[1, 2], [3, 4]])

im2 = ax2.imshow([[1, 2], [3, 4]])
```
