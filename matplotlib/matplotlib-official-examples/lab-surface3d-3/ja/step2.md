# サーフェスプロット用のデータを作成する

このステップでは、サーフェスプロット用のデータを作成します。X と Y の値のメッシュグリッドを作成し、半径距離 R を計算し、`np.sin()`を使って R の値に基づいて Z の値を計算します。

```python
# Create data for the surface plot
X = np.arange(-5, 5, 0.25)
xlen = len(X)
Y = np.arange(-5, 5, 0.25)
ylen = len(Y)
X, Y = np.meshgrid(X, Y)
R = np.sqrt(X**2 + Y**2)
Z = np.sin(R)
```
