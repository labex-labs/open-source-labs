# Mapper des couleurs à des valeurs

Nous pouvons également mapper un tableau de valeurs à des couleurs à l'aide de la fonction `ScalarMappable.set_array`. Nous allons créer un nouvel ensemble de données et un nouvel objet `LineCollection` avec le paramètre `array` défini sur les valeurs de `x`. Nous pouvons ensuite utiliser la méthode `colorbar` de l'objet `Figure` pour ajouter une barre de couleur au graphique.

```python
N = 50
x = np.arange(N)
ys = [x + i for i in x]
segs = [np.column_stack([x, y]) for y in ys]

fig, ax = plt.subplots()
ax.set_xlim(np.min(x), np.max(x))
ax.set_ylim(np.min(ys), np.max(ys))

line_segments = LineCollection(segs, array=x,
                               linewidths=(0.5, 1, 1.5, 2),
                               linestyles='solid')
ax.add_collection(line_segments)
axcb = fig.colorbar(line_segments)
axcb.set_label('Line Number')
ax.set_title('Line Collection with mapped colors')
plt.sci(line_segments)
plt.show()
```
