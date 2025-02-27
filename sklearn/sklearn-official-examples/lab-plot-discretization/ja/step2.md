# データセットを作成する

このステップでは、連続値の入力特徴量と連続値の出力特徴量を持つデータセットを作成します。入力特徴量には `numpy.random.RandomState()` メソッドを使って乱数を生成し、出力特徴量には `numpy.sin()` メソッドを使って生成します。

```python
rnd = np.random.RandomState(42)
X = rnd.uniform(-3, 3, size=100)
y = np.sin(X) + rnd.normal(size=len(X)) / 3
X = X.reshape(-1, 1)
```
