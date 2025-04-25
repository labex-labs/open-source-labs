# マージン付きのプロット作成

Matplotlib の`margins()`メソッドを使用すると、`set_xlim()`および`set_ylim()`メソッドを使用する代わりに、プロットのマージンを設定できます。このステップでは、`set_xlim()`および`set_ylim()`メソッドの代わりに`margins()`メソッドを使用してプロットをズームインおよびズームアウトする方法を学びます。

```python
import matplotlib.pyplot as plt
import numpy as np

def f(t):
    return np.exp(-t) * np.cos(2*np.pi*t)

t1 = np.arange(0.0, 3.0, 0.01)

# マージン付きのサブプロットを作成
ax1 = plt.subplot(212)
ax1.margins(0.05) # デフォルトのマージンは 0.05、値 0 はフィットを意味する
ax1.plot(t1, f(t1))

# ズームアウトしたマージン付きのサブプロットを作成
ax2 = plt.subplot(221)
ax2.margins(2, 2) # 値>0.0 はズームアウト
ax2.plot(t1, f(t1))
ax2.set_title('Zoomed out')

# ズームインしたマージン付きのサブプロットを作成
ax3 = plt.subplot(222)
ax3.margins(x=0, y=-0.25) # (-0.5, 0.0) の値は中央にズームイン
ax3.plot(t1, f(t1))
ax3.set_title('Zoomed in')

plt.show()
```
