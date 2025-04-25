# データの生成

NumPy を使ってデータを生成します。0 から 5 の間の一様分布で 100 個のデータポイントを生成します。閾値を 2.5 に設定し、ブール演算を使ってラベルを生成します。最初の 50 個のデータポイントを学習データとし、残りをテストデータとします。

```python
train_size = 50
rng = np.random.RandomState(0)
X = rng.uniform(0, 5, 100)[:, np.newaxis]
y = np.array(X[:, 0] > 2.5, dtype=int)
```
