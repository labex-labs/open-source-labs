# データの準備

まず、正弦波の関係といくつかのガウスノイズを持つダミーデータを準備します。Numpyの`linspace()`関数を使って、0から6までの間に100個の等間隔の値からなる1次元配列を作成します。その後、`np.newaxis`属性を使って、この1次元配列を形状`(100,1)`の2次元配列に変換します。この配列に`sin()`関数を適用し、配列に6を掛けることで得られる2つ目の正弦波を加えます。そして、Numpyの`normal()`関数を使って、平均0、標準偏差0.1のガウスノイズを加えます。

```python
import numpy as np

rng = np.random.RandomState(1)
X = np.linspace(0, 6, 100)[:, np.newaxis]
y = np.sin(X).ravel() + np.sin(6 * X).ravel() + rng.normal(0, 0.1, X.shape[0])
```
