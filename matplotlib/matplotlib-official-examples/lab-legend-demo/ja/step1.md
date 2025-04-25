# 特定の線に対する凡例の作成

このステップでは、特定の線に対する凡例を作成します。

```python
# 必要なライブラリをインポート
import matplotlib.pyplot as plt
import numpy as np

# グラフ用のデータを定義
t1 = np.arange(0.0, 2.0, 0.1)
t2 = np.arange(0.0, 2.0, 0.01)

# 複数の線を持つプロットを作成
fig, ax = plt.subplots()
l1, = ax.plot(t2, np.exp(-t2))
l2, l3 = ax.plot(t2, np.sin(2 * np.pi * t2), '--o', t1, np.log(1 + t1), '.')
l4, = ax.plot(t2, np.exp(-t2) * np.sin(2 * np.pi * t2),'s-.')

# 2 つの線に対する凡例を作成
ax.legend((l2, l4), ('oscillatory', 'damped'), loc='upper right', shadow=True)

# グラフにラベルとタイトルを追加
ax.set_xlabel('time')
ax.set_ylabel('volts')
ax.set_title('Damped oscillation')

# グラフを表示
plt.show()
```
