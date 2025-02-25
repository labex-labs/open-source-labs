# xとyの変数を定義する

メッシュグリッドを作成するためのxとyの変数を定義します。

```python
dx, dy = 0.05, 0.05
x = np.arange(-3.0, 3.0, dx)
y = np.arange(-3.0, 3.0, dy)
X, Y = np.meshgrid(x, y)
```
