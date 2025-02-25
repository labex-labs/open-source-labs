# x、y、およびzの値を定義する

NumPyを使ってx、y、およびzの値を生成します。まず、thetaとzの値の範囲を定義します。そして、これらの値を使ってr、x、およびyの値を生成します。

```python
theta = np.linspace(-4 * np.pi, 4 * np.pi, 100)
z = np.linspace(-2, 2, 100)
r = z**2 + 1
x = r * np.sin(theta)
y = r * np.cos(theta)
```
