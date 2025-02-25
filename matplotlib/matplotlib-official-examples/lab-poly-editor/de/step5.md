# Erstellen des Plots

Wir müssen den Plot erstellen und das Polygon hinzufügen.

```python
fig, ax = plt.subplots()
ax.add_patch(poly)
p = PolygonInteractor(ax, poly)

ax.set_title('Click and drag a point to move it')
ax.set_xlim((-2, 2))
ax.set_ylim((-2, 2))
plt.show()
```
