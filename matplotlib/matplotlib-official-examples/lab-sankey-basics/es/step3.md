# Personalizar el diagrama de Sankey

Podemos personalizar el diagrama de Sankey cambiando los flujos, etiquetas, orientaciones y otros parámetros. En este ejemplo, crearemos un diagrama con trayectorias más largas y una etiqueta en el centro.

```python
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1, xticks=[], yticks=[],
                     title="Flow Diagram of a Widget")
sankey = Sankey(ax=ax, scale=0.01, offset=0.2, head_angle=180,
                format='%.0f', unit='%')
sankey.add(flows=[25, 0, 60, -10, -20, -5, -15, -10, -40],
           labels=['', '', '', 'First', 'Second', 'Third', 'Fourth',
                   'Fifth', 'Hurray!'],
           orientations=[-1, 1, 0, 1, 1, 1, -1, -1, 0],
           pathlengths=[0.25, 0.25, 0.25, 0.25, 0.25, 0.6, 0.25, 0.25,
                        0.25],
           patchlabel="Widget\nA")  # Argumentos para matplotlib.patches.PathPatch
diagrams = sankey.finish()
diagrams[0].texts[-1].set_color('r')
diagrams[0].text.set_fontweight('bold')
```

Este código creará un diagrama de Sankey con trayectorias más largas, una etiqueta en el centro y otros parámetros personalizados. El diagrama resultante se mostrará con el título "Flow Diagram of a Widget".
