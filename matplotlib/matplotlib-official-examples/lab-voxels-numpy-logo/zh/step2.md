# 定义展开函数

接下来，我们定义一个名为 `explode` 的函数，该函数将用于放大 NumPy 标志的体素图像。此函数接受一个 NumPy 数组作为输入，并返回一个新的 NumPy 数组，其大小是输入数组的两倍。

```python
def explode(data):
    size = np.array(data.shape)*2
    data_e = np.zeros(size - 1, dtype=data.dtype)
    data_e[::2, ::2, ::2] = data
    return data_e
```
