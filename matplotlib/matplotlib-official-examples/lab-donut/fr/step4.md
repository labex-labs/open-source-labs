# Création du beignet

Nous allons créer le beignet en concaténant les sous-chemin intérieur et extérieur. Nous utiliserons `codes` pour spécifier le type de chaque sommet (MOVETO, LINETO, etc.). Nous créerons ensuite un objet `Path` à l'aide de `mpath.Path` et un objet `PathPatch` à l'aide de `mpatches.PathPatch`. Enfin, nous ajouterons l'objet `PathPatch` à l'objet `Axes` à l'aide de `ax.add_patch()`.

```python
Path = mpath.Path
fig, ax = plt.subplots()

inside_vertices = make_circle(0.5)
outside_vertices = make_circle(1.0)
codes = np.ones(
    len(inside_vertices), dtype=mpath.Path.code_type) * mpath.Path.LINETO
codes[0] = mpath.Path.MOVETO

for i, (inside, outside) in enumerate(((1, 1), (1, -1), (-1, 1), (-1, -1))):
    # Concatenate the inside and outside subpaths together, changing their
    # order as needed
    vertices = np.concatenate((outside_vertices[::outside],
                               inside_vertices[::inside]))
    # Shift the path
    vertices[:, 0] += i * 2.5
    # The codes will be all "LINETO" commands, except for "MOVETO"s at the
    # beginning of each subpath
    all_codes = np.concatenate((codes, codes))
    # Create the Path object
    path = mpath.Path(vertices, all_codes)
    # Add plot it
    patch = mpatches.PathPatch(path, facecolor='#885500', edgecolor='black')
    ax.add_patch(patch)

    ax.annotate(f"Outside {wise(outside)},\nInside {wise(inside)}",
                (i * 2.5, -1.5), va="top", ha="center")

ax.set_xlim(-2, 10)
ax.set_ylim(-3, 2)
ax.set_title('Mmm, beignets!')
ax.set_aspect(1.0)
plt.show()
```
