# 生成数据

接下来，我们需要为折线图生成数据。我们将使用 `numpy` 库生成 `r` 和 `theta` 的值数组。

```python
r = np.arange(0, 2, 0.01)
theta = 2 * np.pi * r
```
