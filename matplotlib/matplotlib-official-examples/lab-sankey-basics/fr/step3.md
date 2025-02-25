# Personnaliser le diagramme Sankey

Nous pouvons personnaliser le diagramme Sankey en changeant les flux, les étiquettes, les orientations et d'autres paramètres. Dans cet exemple, nous allons créer un diagramme avec des chemins plus longs et une étiquette au milieu.

```python
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1, xticks=[], yticks=[],
                     title="Diagramme de flux d'un composant")
sankey = Sankey(ax=ax, scale=0.01, offset=0.2, head_angle=180,
                format='%.0f', unit='%')
sankey.add(flows=[25, 0, 60, -10, -20, -5, -15, -10, -40],
           labels=['', '', '', 'Premier', 'Second', 'Troisième', 'Quatrième',
                   'Cinquième', 'Vive!'],
           orientations=[-1, 1, 0, 1, 1, 1, -1, -1, 0],
           pathlengths=[0.25, 0.25, 0.25, 0.25, 0.25, 0.6, 0.25, 0.25,
                        0.25],
           patchlabel="Composant\nA")  # Arguments à matplotlib.patches.PathPatch
diagrams = sankey.finish()
diagrams[0].texts[-1].set_color('r')
diagrams[0].text.set_fontweight('bold')
```

Ce code créera un diagramme Sankey avec des chemins plus longs, une étiquette au milieu et d'autres paramètres personnalisés. Le diagramme résultant sera affiché avec le titre "Diagramme de flux d'un composant".
