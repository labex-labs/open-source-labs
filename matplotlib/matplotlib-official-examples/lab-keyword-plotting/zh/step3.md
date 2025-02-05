# 创建数据

在这一步中，我们将创建一个字典`data`，其中包含变量`a`、`b`、`c`和`d`的值。

```python
data = {'a': np.arange(50),
        'c': np.random.randint(0, 50, 50),
        'd': np.random.randn(50)}

data['b'] = data['a'] + 10 * np.random.randn(50)
data['d'] = np.abs(data['d']) * 100
```
