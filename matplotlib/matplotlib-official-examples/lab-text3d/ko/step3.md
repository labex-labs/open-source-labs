# `~.Axes3D.text` 함수를 `zdir` 값과 함께 사용하기

`~.Axes3D.text` 함수를 사용하여 다양한 `zdir` 값을 가진 텍스트 주석을 배치합니다.

```python
zdirs = (None, 'x', 'y', 'z', (1, 1, 0), (1, 1, 1))
xs = (1, 4, 4, 9, 4, 1)
ys = (2, 5, 8, 10, 1, 2)
zs = (10, 3, 8, 9, 1, 8)

for zdir, x, y, z in zip(zdirs, xs, ys, zs):
    label = '(%d, %d, %d), dir=%s' % (x, y, z, zdir)
    ax.text(x, y, z, label, zdir)
```
