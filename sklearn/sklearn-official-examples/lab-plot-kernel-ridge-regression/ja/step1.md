# サンプルデータを生成する

我々は、正弦波の目的関数と、5番目のデータポイントに強いノイズが加えられたデータセットを生成します。

```python
import numpy as np

# サンプルデータを生成する
rng = np.random.RandomState(42)
X = 5 * rng.rand(10000, 1)
y = np.sin(X).ravel()

# ターゲットにノイズを加える
y[::5] += 3 * (0.5 - rng.rand(X.shape[0] // 5))

X_plot = np.linspace(0, 5, 100000)[:, None]
```
