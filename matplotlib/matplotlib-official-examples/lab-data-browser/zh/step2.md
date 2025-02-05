# 生成数据

我们将使用 NumPy 生成随机数据。

```python
np.random.seed(19680801)
X = np.random.rand(100, 200)
xs = np.mean(X, axis=1)
ys = np.std(X, axis=1)
```
