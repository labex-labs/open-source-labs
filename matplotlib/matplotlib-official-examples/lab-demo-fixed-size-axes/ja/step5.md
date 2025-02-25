# グラフに軸を追加する

`add_axes()` 関数を使って、`Divider` オブジェクトの位置を渡して、グラフに軸を追加します。

```python
ax = fig.add_axes(divider.get_position(),
                  axes_locator=divider.new_locator(nx=1, ny=1))
```
