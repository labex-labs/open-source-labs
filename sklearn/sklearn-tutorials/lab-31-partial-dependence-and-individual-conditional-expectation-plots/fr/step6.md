# Calculez les valeurs de dépendance partielle pour une caractéristique spécifique

```python
x_index = 0
pdp, axes = partial_dependence(model, X, features=[x_index], grid_resolution=20)

# Tracez les valeurs de dépendance partielle
plt.plot(axes[x_index], pdp[0])
plt.xlabel(feature_names[x_index])
plt.ylabel("Dépendance partielle")
plt.title("Graphique de dépendance partielle")

plt.show()
```
