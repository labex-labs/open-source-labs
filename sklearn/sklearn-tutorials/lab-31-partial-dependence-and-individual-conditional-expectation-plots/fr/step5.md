# Créez et visualisez des graphiques d'espérance conditionnelle individuelle

```python
fig, ax = plot_partial_dependence(model, X, features=[(0, 1), (2, 3)], feature_names=feature_names, kind='individual')

# Définissez la taille de la figure et le titre
fig.set_size_inches(10, 8)
fig.suptitle('Graphiques d\'espérance conditionnelle individuelle')

plt.show()
```
