# Créez un graphique

Ensuite, nous allons créer un graphique simple à l'aide de NumPy. Ce graphique servira de fond pour les flèches de direction ancrées.

```python
# Fixing random state for reproducibility
np.random.seed(19680801)

fig, ax = plt.subplots()
ax.imshow(np.random.random((10, 10)))
```
