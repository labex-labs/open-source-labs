# NumPy 固有の配列作成関数を使用する

NumPy は配列を作成するための組み込み関数を提供しています。以下はいくつかの例です。

```python
import numpy as np

# 定期的に増加する値を持つ 1 次元配列を作成する
arr1D = np.arange(10)

# 特定のデータ型を持つ 1 次元配列を作成する
arr1D_float = np.arange(2, 10, dtype=float)

# 指定された要素数の 1 次元配列を作成する
arr1D_linspace = np.linspace(1., 4., 6)

# 2 次元の単位行列を作成する
identity_matrix = np.eye(3)

# 対角線に与えられた値を持つ 2 次元配列を作成する
diag_matrix = np.diag([1, 2, 3])

# バンダーモンド行列を作成する
vander_matrix = np.vander([1, 2, 3, 4], 2)

# ゼロで埋められた配列を作成する
zeros_array = np.zeros((2, 3))

# 1 で埋められた配列を作成する
ones_array = np.ones((2, 3))

# ランダムな値で埋められた配列を作成する
random_array = np.random.default_rng(42).random((2, 3))
```
