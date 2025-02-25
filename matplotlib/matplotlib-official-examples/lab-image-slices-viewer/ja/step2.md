# データを作成する

NumPy の `ogrid` 関数を使って 3D データを作成します。

```python
x, y, z = np.ogrid[-10:10:100j, -10:10:100j, 1:10:20j]
X = np.sin(x * y * z) / (x * y * z)
```
