# Forme de la tête et points d'ancrage fixés dans l'espace d'affichage

Cela est utile si vous annotiez un graphique et que vous ne voulez pas que la flèche change de forme ou de position lorsque vous déplacez ou mettez à l'échelle le graphique.

```python
fig, axs = plt.subplots(nrows=2)
arrow = mpatches.FancyArrowPatch((x_tail, y_tail), (x_head, y_head),
                                 mutation_scale=100,
                                 transform=axs[0].transAxes)
axs[0].add_patch(arrow)

arrow = mpatches.FancyArrowPatch((x_tail, y_tail), (x_head, y_head),
                                 mutation_scale=100,
                                 transform=axs[1].transAxes)
axs[1].add_patch(arrow)
axs[1].set(xlim=(0, 2), ylim=(0, 2))

plt.show()
```
