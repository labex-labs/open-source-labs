# 固定サイズとパディングを持つ独自の軸のグリッドの作成

固定サイズとパディングを持つ独自の軸のグリッドを作成します。`Divider` クラスを使って、軸の矩形を `horiz * vert` で指定されたサイズのグリッドに分割します。その後、`add_axes()` メソッドを使って図に 4 つの軸を追加し、`Divider` クラスの `new_locator()` メソッドを使って各軸の位置を指定します。

```python
# Sizes are in inches.
horiz = [Size.Fixed(1.), Size.Fixed(.5), Size.Fixed(1.5), Size.Fixed(.5)]
vert = [Size.Fixed(1.5), Size.Fixed(.5), Size.Fixed(1.)]

rect = (0.1, 0.1, 0.8, 0.8)
fig = plt.figure(figsize=(6, 6))
fig.suptitle("Fixed axes sizes, fixed paddings")

div = Divider(fig, rect, horiz, vert, aspect=False)

# The rect parameter will actually be ignored and overridden by axes_locator.
ax1 = fig.add_axes(rect, axes_locator=div.new_locator(nx=0, ny=0))
label_axes(ax1, "nx=0, ny=0")
ax2 = fig.add_axes(rect, axes_locator=div.new_locator(nx=0, ny=2))
label_axes(ax2, "nx=0, ny=2")
ax3 = fig.add_axes(rect, axes_locator=div.new_locator(nx=2, ny=2))
label_axes(ax3, "nx=2, ny=2")
ax4 = fig.add_axes(rect, axes_locator=div.new_locator(nx=2, nx1=4, ny=0))
label_axes(ax4, "nx=2, nx1=4, ny=0")

plt.show()
```
