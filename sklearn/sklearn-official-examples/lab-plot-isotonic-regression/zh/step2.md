# 生成数据

接下来，我们将生成一些数据用于回归。我们将创建一个带有同方差均匀噪声的非线性单调趋势。

```python
n = 100
x = np.arange(n)
rs = check_random_state(0)
y = rs.randint(-50, 50, size=(n,)) + 50.0 * np.log1p(np.arange(n))
```
