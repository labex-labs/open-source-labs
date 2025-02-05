# 生成数据

我们将使用 numpy 生成一些随机测试数据。

```python
np.random.seed(19680801)
all_data = [np.random.normal(0, std, 100) for std in range(6, 10)]
```
