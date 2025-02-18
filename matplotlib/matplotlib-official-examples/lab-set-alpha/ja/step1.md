# 明示的なアルファ値を持つ棒グラフの作成

このステップでは、Matplotlib の `bar` メソッドを使用して棒グラフを作成します。`alpha` キーワード引数を使用してアルファ値を設定します。グラフ内のすべての棒は同じアルファ値を持ちます。

```python
import matplotlib.pyplot as plt
import numpy as np

# Fixing random state for reproducibility.
np.random.seed(19680801)

fig, ax = plt.subplots()

x_values = [n for n in range(20)]
y_values = np.random.randn(20)

facecolors = ['green' if y > 0 else 'red' for y in y_values]
edgecolors = facecolors

ax.bar(x_values, y_values, color=facecolors, edgecolor=edgecolors, alpha=0.5)
ax.set_title("Explicit 'alpha' keyword value\nshared by all bars and edges")

plt.show()
```
