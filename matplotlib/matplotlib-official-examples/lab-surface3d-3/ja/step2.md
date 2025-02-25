# サーフェスプロット用のデータを作成する

このステップでは、サーフェスプロット用のデータを作成します。XとYの値のメッシュグリッドを作成し、半径距離Rを計算し、`np.sin()`を使ってRの値に基づいてZの値を計算します。

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
