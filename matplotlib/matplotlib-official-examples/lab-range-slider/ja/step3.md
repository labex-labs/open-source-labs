# RangeSlider を作成する

ここでは、画像のしきい値を調整できる RangeSlider ウィジェットを作成します。スライダー用の新しい軸を作成し、それを図に追加します。

```python
slider_ax = fig.add_axes([0.20, 0.1, 0.60, 0.03])
slider = RangeSlider(slider_ax, "Threshold", img.min(), img.max())
```
