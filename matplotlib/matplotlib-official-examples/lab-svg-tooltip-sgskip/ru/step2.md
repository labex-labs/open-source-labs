# Добавляем фигуры и аннотации для подсказок

Затем мы добавляем фигуры и аннотации для подсказок на график. Аннотации для подсказок создаются с использованием метода `annotate`. Мы задаем параметр `xy` координатами фигуры и `xytext` значением `(0, 0)`, чтобы расположить подсказку непосредственно над фигурой. Также мы задаем параметр `textcoords` значением `'offset points'`, чтобы выровнять подсказку с фигурой. Мы задаем параметр `color` значением `'w'`, чтобы сделать текст белым, `ha` значением `'center'`, чтобы выровнять текст по горизонтали, `fontsize` значением `8`, чтобы установить размер шрифта, и `bbox`, чтобы задать стиль рамки подсказки.

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
