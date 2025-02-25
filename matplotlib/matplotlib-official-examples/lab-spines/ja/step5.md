# 下辺と左辺のスパインのカスタマイズ

2 番目のサブプロットでは、プロットの下辺と左辺のみにスパインを表示します。`set_visible` メソッドを使って、プロットの右辺と上辺のスパインを非表示にすることができます。

```python
ax1.plot(x, y)
ax1.set_title('Bottom-Left Spines')

# Hide the right and top spines
ax1.spines.right.set_visible(False)
ax1.spines.top.set_visible(False)
```
