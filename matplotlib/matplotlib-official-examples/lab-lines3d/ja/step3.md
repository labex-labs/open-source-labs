# x、y、および z の値を定義する

NumPy を使って x、y、および z の値を生成します。まず、theta と z の値の範囲を定義します。そして、これらの値を使って r、x、および y の値を生成します。

```python
theta = np.linspace(-4 * np.pi, 4 * np.pi, 100)
z = np.linspace(-2, 2, 100)
r = z**2 + 1
x = r * np.sin(theta)
y = r * np.cos(theta)
```
