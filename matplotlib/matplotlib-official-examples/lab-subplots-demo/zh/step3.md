# 沿两个方向堆叠子图

要创建子图网格，我们可以将行数和列数作为参数传递给 `subplots()` 函数。返回的 `axs` 对象是一个二维 NumPy 数组。

```python
fig, axs = plt.subplots(2, 2)
axs[0, 0].plot(x, y)
axs[0, 1].plot(x, y, 'tab:orange')
axs[1, 0].plot(x, -y, 'tab:green')
axs[1, 1].plot(x, -y, 'tab:red')
```
