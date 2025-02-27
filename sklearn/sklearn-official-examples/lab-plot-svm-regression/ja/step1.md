# サンプルデータの生成

まず、0から5の間の40個のランダムな値からなるサンプルデータセットを生成します。次に、各値のサイン関数を計算し、5番目の値に対してノイズを追加します。

```python
import numpy as np

# Generate sample data
X = np.sort(5 * np.random.rand(40, 1), axis=0)
y = np.sin(X).ravel()

# add noise to targets
y[::5] += 3 * (0.5 - np.random.rand(8))
```
