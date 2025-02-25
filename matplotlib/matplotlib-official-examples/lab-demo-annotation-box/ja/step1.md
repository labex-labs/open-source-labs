# 点のプロット

始めに、後で注釈を付ける 2 つの点をプロットしましょう。

```python
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()

# 注釈を付ける最初の位置を定義する (マーカーで表示する)
xy1 = (0.5, 0.7)
ax.plot(xy1[0], xy1[1], ".r")

# 注釈を付ける 2 番目の位置を定義する (今回はマーカーで表示しない)
xy2 = [0.3, 0.55]

# すべてを表示するために表示範囲を固定する
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)

plt.show()
```
