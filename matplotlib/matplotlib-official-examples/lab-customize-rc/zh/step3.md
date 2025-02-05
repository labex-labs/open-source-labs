# 创建子图

要在 Matplotlib 中创建子图，你可以使用 `subplot()` 方法。此方法接受三个参数：行数、列数和子图编号。以下是一个创建三个子图的示例：

```python
plt.subplot(311)
plt.plot([1, 2, 3])

plt.subplot(312)
plt.plot([1, 2, 3])
plt.grid(True)

plt.subplot(313)
plt.plot([1, 2, 3])
plt.grid(True)
```
