# Creating the Figure and Axes

Nous allons créer une figure avec deux sous-graphiques (axes) à l'aide de la fonction `subplots`. Nous allons également définir le titre de la figure.

```python
fig, axs = plt.subplots(2, 1)
fig.suptitle('Mouse Hover Over Figure or Axes to Trigger Events')
```
