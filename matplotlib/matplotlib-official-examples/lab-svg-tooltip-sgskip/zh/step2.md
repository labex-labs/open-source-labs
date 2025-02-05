# 添加补丁和工具提示注释

然后，我们将补丁和工具提示注释添加到绘图中。工具提示注释是使用 `annotate` 方法创建的。我们将 `xy` 参数设置为补丁的坐标，将 `xytext` 设置为 `(0, 0)`，以便将工具提示直接定位在补丁上方。我们还将 `textcoords` 参数设置为 `'offset points'`，以使工具提示与补丁对齐。我们将 `color` 参数设置为 `'w'` 以使文本为白色，将 `ha` 设置为 `'center'` 以使文本水平居中，将 `fontsize` 设置为 `8` 以设置字体大小，并使用 `bbox` 设置工具提示框的样式。

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
