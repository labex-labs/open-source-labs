# Erstellen eines Tripcolor-Diagramms

Jetzt werden wir ein Tripcolor-Diagramm mit der `tripcolor()`-Funktion erstellen. Wir werden zwei Diagramme mit unterschiedlichen Schattierungsverfahren erstellen.

```python
# Flat shading plot
fig1, ax1 = plt.subplots()
ax1.set_aspect('equal')
tpc = ax1.tripcolor(triang, z, shading='flat')
fig1.colorbar(tpc)
ax1.set_title('tripcolor of Delaunay triangulation, flat shading')

# Gouraud shading plot
fig2, ax2 = plt.subplots()
ax2.set_aspect('equal')
tpc = ax2.tripcolor(triang, z, shading='gouraud')
fig2.colorbar(tpc)
ax2.set_title('tripcolor of Delaunay triangulation, gouraud shading')
```
