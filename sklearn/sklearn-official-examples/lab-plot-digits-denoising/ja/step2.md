# 学習用とテスト用のセットを作成する

データセットを、サンプル数 1000 の学習用セットと、サンプル数 100 のテスト用セットに分割します。テスト用セットにガウスノイズを加え、元のデータのコピーを 2 つ作成します。1 つはノイズがあるものと、もう 1 つはノイズのないものです。

```python
X_train, X_test, y_train, y_test = train_test_split(
    X, y, stratify=y, random_state=0, train_size=1_000, test_size=100
)

rng = np.random.RandomState(0)
noise = rng.normal(scale=0.25, size=X_test.shape)
X_test_noisy = X_test + noise

noise = rng.normal(scale=0.25, size=X_train.shape)
X_train_noisy = X_train + noise
```
