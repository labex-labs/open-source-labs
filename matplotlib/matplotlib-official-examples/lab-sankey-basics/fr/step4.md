# Connecter deux systèmes dans un diagramme Sankey

Nous pouvons également connecter deux systèmes dans un diagramme Sankey. Dans cet exemple, nous allons créer un diagramme avec deux systèmes connectés.

```python
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1, xticks=[], yticks=[], title="Deux systèmes")
flows = [0.25, 0.15, 0.60, -0.10, -0.05, -0.25, -0.15, -0.10, -0.35]
sankey = Sankey(ax=ax, unit=None)
sankey.add(flows=flows, label='un',
           orientations=[-1, 1, 0, 1, 1, 1, -1, -1, 0])
sankey.add(flows=[-0.25, 0.15, 0.1], label='deux',
           orientations=[-1, -1, -1], prior=0, connect=(0, 0))
diagrams = sankey.finish()
diagrams[-1].patch.set_hatch('/')
plt.legend()
```

Ce code créera un diagramme Sankey avec deux systèmes connectés. Le diagramme résultant sera affiché avec le titre "Deux systèmes".
