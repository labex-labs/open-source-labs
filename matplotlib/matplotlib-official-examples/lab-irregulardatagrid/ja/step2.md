# ランダムなデータを生成する

NumPyの `np.random.uniform` メソッドを使ってランダムなデータを生成します。-2 から 2 の間の x と y の値を持つ `npts = 200` 個のデータポイントを生成します。また、関数 `z = x * np.exp(-x**2 - y**2)` を使って z 値を計算します。

```python
np.random.seed(19680801)
npts = 200
x = np.random.uniform(-2, 2, npts)
y = np.random.uniform(-2, 2, npts)
z = x * np.exp(-x**2 - y**2)
```
