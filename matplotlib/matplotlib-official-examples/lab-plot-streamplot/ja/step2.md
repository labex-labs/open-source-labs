# データの作成

Numpy ライブラリを使って、streamplot 用のデータを作成します。この例では、両方向に 100 点のメッシュグリッドを作成し、ベクトルフィールドの U と V の成分を計算します。

```python
w = 3
Y, X = np.mgrid[-w:w:100j, -w:w:100j]
U = -1 - X**2 + Y
V = 1 + X - Y**2
speed = np.sqrt(U**2 + V**2)
```
