# Ajouter les patches et les annotations du tool-tip

Nous ajoutons ensuite les patches et les annotations du tool-tip à la figure. Les annotations du tool-tip sont créées à l'aide de la méthode `annotate`. Nous définissons le paramètre `xy` sur les coordonnées du patch et `xytext` sur `(0, 0)` pour positionner le tool-tip directement au-dessus du patch. Nous définissons également le paramètre `textcoords` sur `'offset points'` pour aligner le tool-tip avec le patch. Nous définissons le paramètre `color` sur `'w'` pour rendre le texte blanc, `ha` sur `'center'` pour centrer le texte horizontalement, `fontsize` sur `8` pour définir la taille de la police et `bbox` pour définir le style de la boîte du tool-tip.

```python
for i, (item, label) in enumerate(zip(shapes, labels)):
    patch = ax.add_patch(item)
    annotate = ax.annotate(labels[i], xy=item.get_xy(), xytext=(0, 0),
                           textcoords='offset points', color='w', ha='center',
                           fontsize=8, bbox=dict(boxstyle='round, pad=.5',
                                                 fc=(.1,.1,.1,.92),
                                                 ec=(1., 1., 1.), lw=1,
                                                 zorder=1))

    ax.add_patch(patch)
    patch.set_gid(f'mypatch_{i:03d}')
    annotate.set_gid(f'mytooltip_{i:03d}')
```
