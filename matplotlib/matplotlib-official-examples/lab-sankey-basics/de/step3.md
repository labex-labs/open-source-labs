# Anpassen des Sankey-Diagramms

Wir können das Sankey-Diagramm anpassen, indem wir die Ströme, Beschriftungen, Orientierungen und andere Parameter ändern. In diesem Beispiel erstellen wir ein Diagramm mit längeren Pfaden und einer Beschriftung in der Mitte.

```python
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1, xticks=[], yticks=[],
                     title="Flussdiagramm eines Widgets")
sankey = Sankey(ax=ax, scale=0.01, offset=0.2, head_angle=180,
                format='%.0f', unit='%')
sankey.add(flows=[25, 0, 60, -10, -20, -5, -15, -10, -40],
           labels=['', '', '', 'Erster', 'Zweiter', 'Dritter', 'Vierter',
                   'Fünfter', 'Hurra!'],
           orientations=[-1, 1, 0, 1, 1, 1, -1, -1, 0],
           pathlengths=[0.25, 0.25, 0.25, 0.25, 0.25, 0.6, 0.25, 0.25,
                        0.25],
           patchlabel="Widget\nA")  # Argumente für matplotlib.patches.PathPatch
diagrams = sankey.finish()
diagrams[0].texts[-1].set_color('r')
diagrams[0].text.set_fontweight('bold')
```

Dieser Code erzeugt ein Sankey-Diagramm mit längeren Pfaden, einer Beschriftung in der Mitte und anderen angepassten Parametern. Das resultierende Diagramm wird mit dem Titel "Flussdiagramm eines Widgets" angezeigt.
