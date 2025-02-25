# Y2 軸を作成する

最後に、グラフの右側にオフセット (20, 0) で新しい y2 軸を作成し、それにラベルを付けます。

```python
ax.axis["right2"] = ax.new_fixed_axis(loc="right", offset=(20, 0))
ax.axis["right2"].label.set_text("Label Y2")
```
