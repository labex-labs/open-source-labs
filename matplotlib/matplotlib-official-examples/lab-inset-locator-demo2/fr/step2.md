# Créez une figure et des sous-graphiques

Ensuite, nous allons créer une figure et des sous-graphiques pour afficher nos données. Nous allons créer deux sous-graphiques côte à côte pour montrer deux exemples différents d'incrustations zoomées.

```python
fig, (ax, ax2) = plt.subplots(ncols=2, figsize=[6, 3])
```
