# 軸を調整してy軸ラベル用のスペースを確保する

このステップでは、`add_auto_adjustable_area`メソッドを使用して軸を調整し、y軸ラベル用のスペースを確保します。また、2番目の軸のタイトルとx軸ラベルを設定します。

```python
divider.add_auto_adjustable_area(use_axes=[ax1], pad=0.1,
                                 adjust_dirs=["left"])
divider.add_auto_adjustable_area(use_axes=[ax2], pad=0.1,
                                 adjust_dirs=["right"])
divider.add_auto_adjustable_area(use_axes=[ax1, ax2], pad=0.1,
                                 adjust_dirs=["top", "bottom"])

ax1.set_yticks([0.5], labels=["very long label"])
ax2.set_title("Title")
ax2.set_xlabel("X - Label")
```
