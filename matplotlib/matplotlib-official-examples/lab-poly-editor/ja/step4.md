# ポリゴンを作成する

`Polygon` クラスを使って編集するポリゴンを作成する必要があります。

```python
theta = np.arange(0, 2*np.pi, 0.1)
r = 1.5

xs = r * np.cos(theta)
ys = r * np.sin(theta)

poly = Polygon(np.column_stack([xs, ys]), animated=True)
```
