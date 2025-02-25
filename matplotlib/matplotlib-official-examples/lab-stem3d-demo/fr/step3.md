# Créez le graphique en batonnet 3D

Dans cette étape, nous allons créer le graphique en batonnet 3D à l'aide de la fonction `stem` de Matplotlib. Nous passerons les coordonnées x, y et z en tant qu'arguments à la fonction `stem`.

```python
fig, ax = plt.subplots(subplot_kw=dict(projection='3d'))
ax.stem(x, y, z)

plt.show()
```
