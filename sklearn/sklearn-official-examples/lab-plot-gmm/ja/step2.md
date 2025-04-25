# データの生成

このステップでは、異なる平均と共分散を持つ 2 つのガウス分布から構成されるサンプルデータセットを生成します。

```python
n_samples = 500

np.random.seed(0)
C = np.array([[0.0, -0.1], [1.7, 0.4]])
X = np.r_[
    np.dot(np.random.randn(n_samples, 2), C),
    0.7 * np.random.randn(n_samples, 2) + np.array([-6, 3]),
]
```
