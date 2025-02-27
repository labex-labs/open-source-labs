# 学習用データの作成

次に、異なるセクションで使用する学習用データセットを作成します。

```python
rng = np.random.RandomState(4)
X_train = rng.uniform(0, 5, 10).reshape(-1, 1)
y_train = np.sin((X_train[:, 0] - 2.5) ** 2)
n_samples = 5
```
