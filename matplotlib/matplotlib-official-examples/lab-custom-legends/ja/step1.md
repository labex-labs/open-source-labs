# 線の描画

このステップでは、Matplotlibライブラリを使って一連の線を描画します。まず、NumPyを使っていくつかのランダムなデータを作成します。次に、色のサイクルを指定するために `cycler` 関数を使ってカラーマップを設定します。最後に、`plot` 関数を使ってデータを描画し、凡例を生成するために `legend()` を呼び出します。

```python
import matplotlib.pyplot as plt
import numpy as np

# 再現性のために乱数シードを設定
np.random.seed(19680801)

# ランダムなデータを作成
N = 10
data = (np.geomspace(1, 10, 100) + np.random.randn(N, 100)).T

# 色のサイクルを設定
cmap = plt.cm.coolwarm
plt.rcParams['axes.prop_cycle'] = cycler(color=cmap(np.linspace(0, 1, N)))

# データを描画して凡例を生成
fig, ax = plt.subplots()
lines = ax.plot(data)
ax.legend()
```
