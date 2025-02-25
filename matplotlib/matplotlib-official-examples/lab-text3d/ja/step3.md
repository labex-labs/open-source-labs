# `zdir` 値を持つ `~.Axes3D.text` 関数の使用

異なる `zdir` 値を持つテキスト注釈を配置するために、`~.Axes3D.text` 関数を使用します。

```python
zdirs = (None, 'x', 'y', 'z', (1, 1, 0), (1, 1, 1))
xs = (1, 4, 4, 9, 4, 1)
ys = (2, 5, 8, 10, 1, 2)
zs = (10, 3, 8, 9, 1, 8)

for zdir, x, y, z in zip(zdirs, xs, ys, zs):
    label = '(%d, %d, %d), dir=%s' % (x, y, z, zdir)
    ax.text(x, y, z, label, zdir)
```
