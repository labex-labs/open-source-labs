# Afficher l'image et son histogramme

Ensuite, nous allons afficher l'image à l'aide de la fonction `imshow` de Matplotlib, et son histogramme à l'aide de `hist`. Nous allons créer une figure avec deux sous-graphiques, l'un pour l'image et l'autre pour l'histogramme.

```python
fig, axs = plt.subplots(1, 2, figsize=(10, 5))
fig.subplots_adjust(bottom=0.25)

im = axs[0].imshow(img)
axs[1].hist(img.flatten(), bins='auto')
axs[1].set_title('Histogram of pixel intensities')
```
