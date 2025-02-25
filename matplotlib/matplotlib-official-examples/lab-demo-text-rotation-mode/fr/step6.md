# Souligner la boîte englobante du texte

Si le `rotation_mode` est défini sur `'default'`, nous allons souligner la boîte englobante du texte à l'aide d'un rectangle. Nous utiliserons la fonction `get_window_extent` pour obtenir la boîte englobante et la transformer en coordonnées de données à l'aide de l'attribut `transData`.

```python
if mode == "default":
    fig.canvas.draw()
    for ax, text in texts.items():
        bb = text.get_window_extent().transformed(ax.transData.inverted())
        rect = plt.Rectangle((bb.x0, bb.y0), bb.width, bb.height,
                             facecolor="C1", alpha=0.3, zorder=2)
        ax.add_patch(rect)
```
