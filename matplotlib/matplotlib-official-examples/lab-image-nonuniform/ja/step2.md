# 線形と非線形の配列を作成する

線形の値を持つ配列と非線形の値を持つ配列の 2 つを作成する必要があります。これらの配列は、NonUniformImage を作成するために使用されます。

```python
# セル中心の線形 x 配列：
x = np.linspace(-4, 4, 9)

# 高度に非線形な x 配列：
x2 = x**3

y = np.linspace(-4, 4, 9)

z = np.sqrt(x[np.newaxis, :]**2 + y[:, np.newaxis]**2)
```
