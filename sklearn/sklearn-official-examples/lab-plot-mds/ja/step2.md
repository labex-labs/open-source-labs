# データの生成

次に、numpy を使ってノイズ付きのデータセットを生成します。2 つの特徴量を持つ 20 個のサンプルを生成します。

```python
EPSILON = np.finfo(np.float32).eps
n_samples = 20
seed = np.random.RandomState(seed=3)
X_true = seed.randint(0, 20, 2 * n_samples).astype(float)
X_true = X_true.reshape((n_samples, 2))
# データを中心化する
X_true -= X_true.mean()
```
