# 矢印の方向を定義する

次に、矢印の方向を定義します。この例では、NumPyの三角関数を使って矢印の方向を定義します。`sin`関数と`cos`関数は、`x`、`y`、`z`方向の矢印の方向を表す`u`、`v`、`w`配列を作成するために使用されます。

```python
u = np.sin(np.pi * x) * np.cos(np.pi * y) * np.cos(np.pi * z)
v = -np.cos(np.pi * x) * np.sin(np.pi * y) * np.cos(np.pi * z)
w = (np.sqrt(2.0 / 3.0) * np.cos(np.pi * x) * np.cos(np.pi * y) *
     np.sin(np.pi * z))
```
