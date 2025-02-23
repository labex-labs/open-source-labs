# ランダムなデータを生成する

`numpy.random.random()` を使って、ランダムなデータの 3 次元配列を生成します。コードを実行するたびに同じデータセットが生成されるように、シード値を使用します。

```python
np.random.seed(19680801)
data = np.random.random((50, 50, 50))
```
