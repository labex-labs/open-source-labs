# 解析的なテスト関数

このステップでは、Triangulationに対するz値を生成するために使用される解析的なテスト関数を定義します。この関数は`function_z`と呼ばれ、2つの引数`x`と`y`を取ります。この関数は`x`と`y`の値に基づいて`z`を計算し、正規化された`z`値を返します。

```python
def function_z(x, y):
    r1 = np.sqrt((0.5 - x)**2 + (0.5 - y)**2)
    theta1 = np.arctan2(0.5 - x, 0.5 - y)
    r2 = np.sqrt((-x - 0.2)**2 + (-y - 0.2)**2)
    theta2 = np.arctan2(-x - 0.2, -y - 0.2)
    z = -(2 * (np.exp((r1 / 10)**2) - 1) * 30. * np.cos(7. * theta1) +
          (np.exp((r2 / 10)**2) - 1) * 30. * np.cos(11. * theta2) +
          0.7 * (x**2 + y**2))
    return (np.max(z) - z) / (np.max(z) - np.min(z))
```
