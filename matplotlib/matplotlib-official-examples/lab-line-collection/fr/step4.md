# Création d'un graphique

Nous pouvons maintenant créer un graphique à l'aide de `matplotlib` et ajouter l'objet `LineCollection` au graphique en utilisant la méthode `add_collection` de l'objet `Axes`.

```python
fig, ax = plt.subplots()
ax.set_xlim(x.min(), x.max())
ax.set_ylim(ys.min(), ys.max())

ax.add_collection(line_segments)
ax.set_title('Line collection with masked arrays')
plt.show()
```
