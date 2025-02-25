# データの生成

NumPyを使ってランダムなデータを生成します。

```python
np.random.seed(19680801)
X = np.random.rand(100, 200)
xs = np.mean(X, axis=1)
ys = np.std(X, axis=1)
```
