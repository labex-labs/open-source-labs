# テスト用のデータポイントを生成する

-1から1の間のxとyの値を持つ、ランダムなテスト用のデータポイントのセットを生成します。また、手順2で定義した`experiment_res`関数を使用して、対応するz値のセットも生成します。

```python
# User parameters for data test points

# Number of test data points, tested from 3 to 5000 for subdiv=3
n_test = 200

# Random points
random_gen = np.random.RandomState(seed=19680801)
x_test = random_gen.uniform(-1., 1., size=n_test)
y_test = random_gen.uniform(-1., 1., size=n_test)
z_test = experiment_res(x_test, y_test)
```
