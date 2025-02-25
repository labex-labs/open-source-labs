# Fügen Sie Patches und Tooltip-Anmerkungen hinzu

Wir fügen dann die Patches und die Tooltip-Anmerkungen zum Graphen hinzu. Die Tooltip-Anmerkungen werden mit der `annotate`-Methode erstellt. Wir legen den `xy`-Parameter auf die Koordinaten des Patches und `xytext` auf `(0, 0)` fest, um den Tooltip direkt über dem Patch zu positionieren. Wir legen auch den `textcoords`-Parameter auf `'offset points'` fest, um den Tooltip mit dem Patch auszurichten. Wir legen den `color`-Parameter auf `'w'` fest, um den Text weiß zu machen, `ha` auf `'center'` fest, um den Text horizontal zentriert zu positionieren, `fontsize` auf `8` fest, um die Schriftgröße einzustellen und `bbox` fest, um den Stil der Tooltip-Box zu setzen.

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
