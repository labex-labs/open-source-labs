# Add patches and tooltip annotations

We then add the patches and tooltip annotations to the plot. The tooltip annotations are created using the `annotate` method. We set the `xy` parameter to the coordinates of the patch and `xytext` to `(0, 0)` to position the tooltip directly over the patch. We also set the `textcoords` parameter to `'offset points'` to align the tooltip with the patch. We set the `color` parameter to `'w'` to make the text white, `ha` to `'center'` to center the text horizontally, `fontsize` to `8` to set the font size, and `bbox` to set the style of the tooltip box.

```python
for i, (item, label) in enumerate(zip(shapes, labels)):
    patch = ax.add_patch(item)
    annotate = ax.annotate(labels[i], xy=item.get_xy(), xytext=(0, 0),
                           textcoords='offset points', color='w', ha='center',
                           fontsize=8, bbox=dict(boxstyle='round, pad=.5',
                                                 fc=(.1, .1, .1, .92),
                                                 ec=(1., 1., 1.), lw=1,
                                                 zorder=1))

    ax.add_patch(patch)
    patch.set_gid(f'mypatch_{i:03d}')
    annotate.set_gid(f'mytooltip_{i:03d}')
```
