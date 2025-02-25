# 浮動軸の追加

浮動軸をプロットに追加する 2 つの関数を定義します。最初の関数 `add_floating_axis1()` は、`theta = 30` のラベル付きで浮動軸をプロットに追加します。2 番目の関数 `add_floating_axis2()` は、`r = 6` のラベル付きで浮動軸をプロットに追加します。

```python
def add_floating_axis1(ax):
    ax.axis["lat"] = axis = ax.new_floating_axis(0, 30)
    axis.label.set_text(r"$\theta = 30^{\circ}$")
    axis.label.set_visible(True)
    return axis

def add_floating_axis2(ax):
    ax.axis["lon"] = axis = ax.new_floating_axis(1, 6)
    axis.label.set_text(r"$r = 6$")
    axis.label.set_visible(True)
    return axis
```
