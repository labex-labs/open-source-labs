# データ範囲に制限された境界でスパインをカスタマイズする

3 番目のサブプロットでは、境界がデータ範囲に制限されたスパインを表示します。`set_bounds` メソッドを使って、各スパインの範囲をデータ範囲に制限することができます。

```python
ax2.plot(x, y)
ax2.set_title('Spines with Bounds Limited to Data Range')

# Only draw spines for the data range, not in the margins
ax2.spines.bottom.set_bounds(x.min(), x.max())
ax2.spines.left.set_bounds(y.min(), y.max())
# Hide the right and top spines
ax2.spines.right.set_visible(False)
ax2.spines.top.set_visible(False)
```
