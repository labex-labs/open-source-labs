# `axhspan`と`axvspan`を使ったAxesの範囲の強調表示

塗りつぶされた領域のもう一つの便利な使い方は、Axesの水平または垂直の範囲を強調表示することです。そのためにMatplotlibにはヘルパー関数`axhspan`と`axvspan`があります。詳細については、`axhspan_demo`ギャラリーを参照してください。

```python
import matplotlib.pyplot as plt

fig, ax = plt.subplots()

ax.axhspan(0.25, 0.75, facecolor='0.5', alpha=0.5)
ax.axvspan(6, 7, facecolor='r', alpha=0.5)

plt.show()
```
