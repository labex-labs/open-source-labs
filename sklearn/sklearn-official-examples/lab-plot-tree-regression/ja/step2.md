# ランダムなデータセットを作成する

NumPy を使ってランダムなデータセットを作成し、それにいくらかのノイズを加えます。

```python
rng = np.random.RandomState(1)
X = np.sort(5 * rng.rand(80, 1), axis=0)
y = np.sin(X).ravel()
y[::5] += 3 * (0.5 - rng.rand(16))
```
