# Tracer l'histogramme de l'intensité de l'IRM

Ensuite, nous allons tracer l'histogramme de l'intensité de l'IRM à l'aide de la fonction `hist()`. Nous allons normaliser les valeurs d'intensité pour qu'elles se situent entre 0 et 1.

```python
# Tracer l'histogramme de l'intensité de l'IRM
ax1 = fig.add_subplot(2, 2, 2)
im = np.ravel(im)
im = im[np.nonzero(im)]  # Ignorer l'arrière-plan
im = im / im.max()  # Normaliser
ax1.hist(im, bins=100)
ax1.set_xlabel('Intensité (a.u.)')
ax1.set_ylabel('Densité IRM')
```
