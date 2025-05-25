# Destacar a caixa delimitadora (bounding box) do texto

Se o `rotation_mode` estiver definido como `'default'`, destacaremos a caixa delimitadora do texto usando um retângulo. Usaremos a função `get_window_extent` para obter a caixa delimitadora e transformá-la para as coordenadas de dados usando o atributo `transData`.

```python
if mode == "default":
    fig.canvas.draw()
    for ax, text in texts.items():
        bb = text.get_window_extent().transformed(ax.transData.inverted())
        rect = plt.Rectangle((bb.x0, bb.y0), bb.width, bb.height,
                             facecolor="C1", alpha=0.3, zorder=2)
        ax.add_patch(rect)
```
