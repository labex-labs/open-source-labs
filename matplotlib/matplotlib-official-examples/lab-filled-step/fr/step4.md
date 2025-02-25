# Configurez la fonction d'histogramme avec des bins fixes

Nous allons configurer une fonction d'histogramme avec des bins fixes en utilisant `numpy.histogram`. Nous allons créer 20 bins allant de -3 à 3.

```python
edges = np.linspace(-3, 3, 20, endpoint=True)
hist_func = partial(np.histogram, bins=edges)
```
