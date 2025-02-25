# y軸ラベル用のスペースを確保して軸を調整する

このステップでは、`make_axes_area_auto_adjustable`メソッドを使用して、両方の軸にy軸ラベル用のスペースを確保します。また、`use_axes`パラメータを使用して調整対象の軸を指定し、`pad`パラメータを使用して軸間の間隔を調整します。

```python
make_axes_area_auto_adjustable(ax1, pad=0.1, use_axes=[ax1, ax2])
make_axes_area_auto_adjustable(ax2, pad=0.1, use_axes=[ax1, ax2])
```
