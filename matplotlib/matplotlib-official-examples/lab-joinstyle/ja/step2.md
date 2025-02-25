# グラフの作成

グラフを作成するには、まず描画したいデータを定義する必要があります。この例では、サンプルデータを生成するために `numpy` ライブラリを使用します。

```python
import numpy as np

x = np.linspace(0, 10, 1000)
y = np.sin(x)
```

次に、`plt.subplots()` を使用して新しい figure と axis を作成します。グラフの x 軸と y 軸の範囲を設定した後、`plot()` を使用してデータを描画します。

```python
fig, ax = plt.subplots()
ax.set_xlim([0, 10])
ax.set_ylim([-1.2, 1.2])
ax.plot(x, y)
```
