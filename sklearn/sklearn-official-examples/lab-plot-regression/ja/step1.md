# サンプルデータを生成する

まず、回帰問題に使用するサンプルデータを生成します。1 つの特徴量を持つ 40 個のデータポイントの配列を作成し、そのデータに正弦関数を適用することで目的変数の配列を作成します。また、5 番目のデータポイントにはノイズを追加します。

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn import neighbors

np.random.seed(0)
X = np.sort(5 * np.random.rand(40, 1), axis=0)
T = np.linspace(0, 5, 500)[:, np.newaxis]
y = np.sin(X).ravel()

# Add noise to targets
y[::5] += 1 * (0.5 - np.random.rand(8))
```
