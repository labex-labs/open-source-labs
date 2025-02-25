# プロット幅に応じて矢印がスケーリングされる（ビューではない）

`quiver()`関数を使用してクイバープロットを作成できます。デフォルトでは、プロット内の矢印はデータに応じてスケーリングされ、プロット自体に応じてスケーリングされるわけではありません。これにより、プロットの端に近い矢印を見るのが困難になる場合があります。

```python
import matplotlib.pyplot as plt
import numpy as np

X, Y = np.meshgrid(np.arange(0, 2 * np.pi,.2), np.arange(0, 2 * np.pi,.2))
U = np.cos(X)
V = np.sin(Y)

fig1, ax1 = plt.subplots()
ax1.set_title('Arrows scale with plot width, not view')
Q = ax1.quiver(X, Y, U, V, units='width')
qk = ax1.quiverkey(Q, 0.9, 0.9, 2, r'$2 \frac{m}{s}$', labelpos='E',
                   coordinates='figure')
plt.show()
```
