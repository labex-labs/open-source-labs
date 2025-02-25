# 軸の方向の変更

次に、4 つの基本方向それぞれに浮動軸を持つ 4 つの異なるプロットを設定するためのループを作成します。ループ内では、浮動軸を追加するために `add_floating_axis1()` と `add_floating_axis2()` を使用し、軸の方向を設定するために `set_axis_direction()` を使用します。

```python
fig = plt.figure(figsize=(8, 4), layout="constrained")

for i, d in enumerate(["bottom", "left", "top", "right"]):
    ax = setup_axes(fig, rect=241+i)
    axis = add_floating_axis1(ax)
    axis.set_axis_direction(d)
    ax.set(title=d)

for i, d in enumerate(["bottom", "left", "top", "right"]):
    ax = setup_axes(fig, rect=245+i)
    axis = add_floating_axis2(ax)
    axis.set_axis_direction(d)
    ax.set(title=d)

plt.show()
```
