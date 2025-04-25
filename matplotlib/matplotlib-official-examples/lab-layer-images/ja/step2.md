# x と y の変数を定義する

メッシュグリッドを作成するための x と y の変数を定義します。

```python
dx, dy = 0.05, 0.05
x = np.arange(-3.0, 3.0, dx)
y = np.arange(-3.0, 3.0, dy)
X, Y = np.meshgrid(x, y)
```
