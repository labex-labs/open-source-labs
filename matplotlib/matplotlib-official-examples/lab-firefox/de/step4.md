# Erstellen des Diagramms

Wir werden nun das Diagramm mit Matplotlib erstellen, indem wir zwei `PathPatch`-Objekte zum Diagramm hinzufügen. Ein Objekt wird eine orange gefüllte Form sein, während das andere eine weiße Umrandung darstellt.

```python
# Setzen der Diagrammgrenzen
xmin, ymin = verts.min(axis=0) - 1
xmax, ymax = verts.max(axis=0) + 1

# Erstellen des Diagramms
fig = plt.figure(figsize=(5, 5), facecolor="0.75")  # grauer Hintergrund
ax = fig.add_axes([0, 0, 1, 1], frameon=False, aspect=1,
                  xlim=(xmin, xmax),  # Zentrierung
                  ylim=(ymax, ymin),  # Zentrierung, gedreht nach oben
                  xticks=[], yticks=[])  # keine Striche

# Hinzufügen der weißen Umrandung
ax.add_patch(patches.PathPatch(path, facecolor='none', edgecolor='w', lw=6))

# Hinzufügen der orangen Form
ax.add_patch(patches.PathPatch(path, facecolor='orange', edgecolor='k', lw=2))

# Anzeigen des Diagramms
plt.show()
```
