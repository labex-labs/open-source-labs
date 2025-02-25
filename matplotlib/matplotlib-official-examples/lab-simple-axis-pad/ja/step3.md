# 浮動軸を追加する関数を定義する

グラフに浮動軸を追加する`add_floating_axis`関数を定義します。この関数は、引数として`ax1`オブジェクトを受け取り、`axis`オブジェクトを返します。

```python
def add_floating_axis(ax1):
    # Define the floating axis
    ax1.axis["lat"] = axis = ax1.new_floating_axis(0, 30)
    axis.label.set_text(r"$\theta = 30^{\circ}$")
    axis.label.set_visible(True)

    return axis
```
