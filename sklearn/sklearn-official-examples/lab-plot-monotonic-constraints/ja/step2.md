# データの生成

目的値が最初の特徴量と正の相関関係を持ち、2番目の特徴量と負の相関関係を持つ人工的なデータセットを生成します。また、データをより現実的にするためにいくつかのランダムノイズを追加します。

```python
rng = np.random.RandomState(0)

n_samples = 1000
f_0 = rng.rand(n_samples)
f_1 = rng.rand(n_samples)
X = np.c_[f_0, f_1]
noise = rng.normal(loc=0.0, scale=0.01, size=n_samples)

y = 5 * f_0 + np.sin(10 * np.pi * f_0) - 5 * f_1 - np.cos(10 * np.pi * f_1) + noise
```
