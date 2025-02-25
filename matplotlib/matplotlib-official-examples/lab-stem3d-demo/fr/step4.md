# Personnalisez le tracé

Dans cette étape, nous allons personnaliser le graphique en batonnet 3D en changeant la ligne de base à l'aide du paramètre `bottom` et en changeant le format à l'aide des paramètres `linefmt`, `markerfmt` et `basefmt`.

```python
fig, ax = plt.subplots(subplot_kw=dict(projection='3d'))
markerline, stemlines, baseline = ax.stem(
    x, y, z, linefmt='grey', markerfmt='D', bottom=np.pi)
markerline.set_markerfacecolor('none')

plt.show()
```
