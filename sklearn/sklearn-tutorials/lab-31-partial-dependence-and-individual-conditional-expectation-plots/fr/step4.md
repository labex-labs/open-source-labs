# Créez et visualisez des graphiques de dépendance partielle

```python
fig, ax = plot_partial_dependence(model, X, features=[(0, 1), (2, 3)], feature_names=feature_names, grid_resolution=20)

# Définissez la taille de la figure et le titre
fig.set_size_inches(10, 8)
fig.suptitle('Graphiques de dépendance partielle')

plt.show()
```
