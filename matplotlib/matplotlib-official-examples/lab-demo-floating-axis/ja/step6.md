# 軸の制限を設定してグリッドを表示する

このステップでは、軸の制限を設定してグリッドを表示します。軸のアスペクト比を設定するには `set_aspect()` を、グリッドを表示するには `grid()` を使用します。

```python
# Set the limits and display the grid
ax1.set_aspect(1.)
ax1.set_xlim(-5, 12)
ax1.set_ylim(-5, 10)
ax1.grid(True)
```
