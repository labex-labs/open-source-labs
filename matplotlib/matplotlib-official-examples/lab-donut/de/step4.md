# Erstellen des Donuts

Wir werden den Donut erstellen, indem wir die inneren und äußeren Teilpfade zusammenfügen. Wir werden `codes` verwenden, um den Typ jedes Eckpunkts (MOVETO, LINETO usw.) anzugeben. Anschließend werden wir ein `Path`-Objekt mit `mpath.Path` und ein `PathPatch`-Objekt mit `mpatches.PathPatch` erstellen. Schließlich werden wir das `PathPatch`-Objekt mit `ax.add_patch()` zum `Axes`-Objekt hinzufügen.

```python
Path = mpath.Path
fig, ax = plt.subplots()

inside_vertices = make_circle(0.5)
outside_vertices = make_circle(1.0)
codes = np.ones(
    len(inside_vertices), dtype=mpath.Path.code_type) * mpath.Path.LINETO
codes[0] = mpath.Path.MOVETO

for i, (inside, outside) in enumerate(((1, 1), (1, -1), (-1, 1), (-1, -1))):
    # Fügen Sie die inneren und äußeren Teilpfade zusammen, und ändern Sie ihre
    # Reihenfolge nach Bedarf
    vertices = np.concatenate((outside_vertices[::outside],
                               inside_vertices[::inside]))
    # Verschieben Sie den Pfad
    vertices[:, 0] += i * 2.5
    # Die Codes werden alle "LINETO"-Anweisungen sein, außer "MOVETO" am
    # Anfang jedes Teilpfads
    all_codes = np.concatenate((codes, codes))
    # Erstellen Sie das Path-Objekt
    path = mpath.Path(vertices, all_codes)
    # Fügen Sie es hinzu und zeichnen Sie es
    patch = mpatches.PathPatch(path, facecolor='#885500', edgecolor='black')
    ax.add_patch(patch)

    ax.annotate(f"Außen {wise(outside)},\nInnen {wise(inside)}",
                (i * 2.5, -1.5), va="top", ha="center")

ax.set_xlim(-2, 10)
ax.set_ylim(-3, 2)
ax.set_title('Mmm, donuts!')
ax.set_aspect(1.0)
plt.show()
```
