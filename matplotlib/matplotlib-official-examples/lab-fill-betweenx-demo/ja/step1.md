# シンプルな fill_betweenx のプロット作成

このステップでは、`fill_betweenx` 関数を使ってシンプルなプロットを作成する方法を学びます。2 つの曲線の間の領域を塗りつぶします。

```python
import matplotlib.pyplot as plt
import numpy as np

y = np.arange(0.0, 2, 0.01)
x1 = np.sin(2 * np.pi * y)
x2 = 1.2 * np.sin(4 * np.pi * y)

fig, ax = plt.subplots(figsize=(6, 6))

ax.fill_betweenx(y, x1, x2, color='green', alpha=0.5)
ax.plot(x1, y, color='blue')
ax.plot(x2, y, color='red')

plt.show()
```
