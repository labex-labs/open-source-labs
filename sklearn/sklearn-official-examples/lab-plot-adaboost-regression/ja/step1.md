# データの準備

まず、正弦波の関係といくつかのガウスノイズを持つダミーデータを準備します。Numpy の`linspace()`関数を使って、0 から 6 までの間に 100 個の等間隔の値からなる 1 次元配列を作成します。その後、`np.newaxis`属性を使って、この 1 次元配列を形状`(100,1)`の 2 次元配列に変換します。この配列に`sin()`関数を適用し、配列に 6 を掛けることで得られる 2 つ目の正弦波を加えます。そして、Numpy の`normal()`関数を使って、平均 0、標準偏差 0.1 のガウスノイズを加えます。

```python
import numpy as np

rng = np.random.RandomState(1)
X = np.linspace(0, 6, 100)[:, np.newaxis]
y = np.sin(X).ravel() + np.sin(6 * X).ravel() + rng.normal(0, 0.1, X.shape[0])
```
