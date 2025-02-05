# 创建信号

我们将使用 NumPy 创建一个信号。我们将使用 linspace 函数创建一个数组 xdata，其起始值为 16，终止值为 365，元素数量为 (365 - 16) \* 4。我们将使用 sin 和 cos 函数创建一个数组 ydata。

```python
xdata = np.linspace(16, 365, (365-16)*4)
ydata = np.sin(2*np.pi*xdata/153) + np.cos(2*np.pi*xdata/127)
```
