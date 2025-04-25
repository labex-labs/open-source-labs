# データの作成

次に、線を描画するために使うデータを作成する必要があります。`numpy` を使って `x` と `y` の値の 2 次元配列を作成します。

```python
x = np.arange(100)
ys = x[:50, np.newaxis] + x[np.newaxis, :]
```
