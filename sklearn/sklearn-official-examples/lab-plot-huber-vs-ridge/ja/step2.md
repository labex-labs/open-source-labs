# 疑似データを生成する

ここでは、scikit-learnのmake_regression関数を使って疑似データセットを生成します。20個のサンプル、1つの特徴量、乱数シード0を持つデータセットを生成します。また、データセットにいくらかのノイズを加えます。

```python
rng = np.random.RandomState(0)
X, y = make_regression(
    n_samples=20, n_features=1, random_state=0, noise=4.0, bias=100.0
)
```
