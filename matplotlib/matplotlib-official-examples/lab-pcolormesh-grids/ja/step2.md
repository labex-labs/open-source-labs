# 可視化用のデータを作成する

次に、可視化に使用する 2 次元グリッドを作成します。NumPy の`meshgrid`関数を使用してグリッドを作成できます。`meshgrid`関数は、グリッド点の座標を表す 2 つのベクトル`x`と`y`が与えられたときに点のグリッドを作成します。次のコードブロックを使用して 5x5 の点のグリッドを作成します。

```python
nrows = 5
ncols = 5
x = np.arange(ncols + 1)
y = np.arange(nrows + 1)
X, Y = np.meshgrid(x, y)
Z = X + Y
```
