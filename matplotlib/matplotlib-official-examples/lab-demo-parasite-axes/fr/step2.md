# Créez une figure et ajoutez des axes hôtes

Nous créons une figure en utilisant la méthode `plt.figure()` et ajoutons un axe hôte en utilisant la méthode `fig.add_axes()`. Les axes hôtes partagent l'échelle x avec les axes parasites.

```python
fig = plt.figure()
host = fig.add_axes([0.15, 0.1, 0.65, 0.8], axes_class=HostAxes)
```
