# 目盛りラベルの設定

デフォルトでは、負の値の目盛りラベルはASCIIのハイフンではなくUnicodeのマイナスを使ってレンダリングされます。ただし、`axes.unicode_minus`を`False`に設定することでこの動作を変更できます。

```python
plt.rcParams['axes.unicode_minus'] = False
```
