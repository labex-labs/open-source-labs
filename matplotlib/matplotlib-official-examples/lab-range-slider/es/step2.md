# Mostrar la imagen y su histograma

A continuación, mostraremos la imagen utilizando la función `imshow` de Matplotlib y su histograma utilizando `hist`. Crearemos una figura con dos subtramas, una para la imagen y otra para el histograma.

```python
fig, axs = plt.subplots(1, 2, figsize=(10, 5))
fig.subplots_adjust(bottom=0.25)

im = axs[0].imshow(img)
axs[1].hist(img.flatten(), bins='auto')
axs[1].set_title('Histogram of pixel intensities')
```
