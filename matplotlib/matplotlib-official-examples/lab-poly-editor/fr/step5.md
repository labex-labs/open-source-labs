# Créez la figure

Nous devons créer la figure et y ajouter le polygone.

```python
fig, ax = plt.subplots()
ax.add_patch(poly)
p = PolygonInteractor(ax, poly)

ax.set_title('Cliquez et faites glisser un point pour le déplacer')
ax.set_xlim((-2, 2))
ax.set_ylim((-2, 2))
plt.show()
```
