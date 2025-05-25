# Conectar dois sistemas em um diagrama de Sankey

Também podemos conectar dois sistemas em um diagrama de Sankey. Neste exemplo, criaremos um diagrama com dois sistemas que estão conectados.

```python
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1, xticks=[], yticks=[], title="Two Systems")
flows = [0.25, 0.15, 0.60, -0.10, -0.05, -0.25, -0.15, -0.10, -0.35]
sankey = Sankey(ax=ax, unit=None)
sankey.add(flows=flows, label='one',
           orientations=[-1, 1, 0, 1, 1, 1, -1, -1, 0])
sankey.add(flows=[-0.25, 0.15, 0.1], label='two',
           orientations=[-1, -1, -1], prior=0, connect=(0, 0))
diagrams = sankey.finish()
diagrams[-1].patch.set_hatch('/')
plt.legend()
```

Este código criará um diagrama de Sankey com dois sistemas que estão conectados. O diagrama resultante será exibido com o título "Two Systems."
