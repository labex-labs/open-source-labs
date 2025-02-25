# Verbinden von zwei Systemen in einem Sankey-Diagramm

Wir können auch zwei Systeme in einem Sankey-Diagramm verbinden. In diesem Beispiel erstellen wir ein Diagramm mit zwei verbundenen Systemen.

```python
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1, xticks=[], yticks=[], title="Zwei Systeme")
flows = [0.25, 0.15, 0.60, -0.10, -0.05, -0.25, -0.15, -0.10, -0.35]
sankey = Sankey(ax=ax, unit=None)
sankey.add(flows=flows, label='eins',
           orientations=[-1, 1, 0, 1, 1, 1, -1, -1, 0])
sankey.add(flows=[-0.25, 0.15, 0.1], label='zwei',
           orientations=[-1, -1, -1], prior=0, connect=(0, 0))
diagrams = sankey.finish()
diagrams[-1].patch.set_hatch('/')
plt.legend()
```

Dieser Code erzeugt ein Sankey-Diagramm mit zwei verbundenen Systemen. Das resultierende Diagramm wird mit dem Titel "Zwei Systeme" angezeigt.
