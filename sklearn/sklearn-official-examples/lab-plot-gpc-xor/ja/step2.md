# XOR データセットの作成

このステップでは、numpy を使って XOR データセットを作成します。入力特徴に基づいてラベルを作成するために logical_xor 関数を使います。

```python
xx, yy = np.meshgrid(np.linspace(-3, 3, 50), np.linspace(-3, 3, 50))
rng = np.random.RandomState(0)
X = rng.randn(200, 2)
Y = np.logical_xor(X[:, 0] > 0, X[:, 1] > 0)
```
