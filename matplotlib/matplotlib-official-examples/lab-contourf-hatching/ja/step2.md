# データの作成

次に、プロットするサンプルデータを作成します。この例では、x と y の値の 2 次元グリッドを作成し、それらを使って z の値を計算します。

```python
# invent some numbers, turning the x and y arrays into simple
# 2d arrays, which make combining them together easier.
x = np.linspace(-3, 5, 150).reshape(1, -1)
y = np.linspace(-3, 5, 120).reshape(-1, 1)
z = np.cos(x) + np.sin(y)
```
