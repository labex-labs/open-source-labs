# データの生成

NumPyを使ってデータを生成します。0から5の間の一様分布で100個のデータポイントを生成します。閾値を2.5に設定し、ブール演算を使ってラベルを生成します。最初の50個のデータポイントを学習データとし、残りをテストデータとします。

```python
train_size = 50
rng = np.random.RandomState(0)
X = rng.uniform(0, 5, 100)[:, np.newaxis]
y = np.array(X[:, 0] > 2.5, dtype=int)
```
