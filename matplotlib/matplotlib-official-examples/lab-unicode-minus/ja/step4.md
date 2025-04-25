# 目盛りラベルの設定

デフォルトでは、負の値の目盛りラベルは ASCII のハイフンではなく Unicode のマイナスを使ってレンダリングされます。ただし、`axes.unicode_minus`を`False`に設定することでこの動作を変更できます。

```python
plt.rcParams['axes.unicode_minus'] = False
```
