# 外側の罫線のみを表示する

このステップでは、内側のサブプロットの罫線を削除し、外側の罫線のみを表示します。これにより、グラフがクリーンに見えるようになります。

```python
for ax in fig.get_axes():
    ss = ax.get_subplotspec()
    ax.spines.top.set_visible(ss.is_first_row())
    ax.spines.bottom.set_visible(ss.is_last_row())
    ax.spines.left.set_visible(ss.is_first_col())
    ax.spines.right.set_visible(ss.is_last_col())
```
