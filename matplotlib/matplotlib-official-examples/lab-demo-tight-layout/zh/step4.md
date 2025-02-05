# 创建多个图表

我们也可以在同一图形中创建多个图表。

```python
x = [1, 2, 3, 4, 5]
y1 = [2, 4, 6, 8, 10]
y2 = [1, 3, 5, 7, 9]

plt.subplot(1, 2, 1)
plt.plot(x, y1)
plt.title('图表 1')

plt.subplot(1, 2, 2)
plt.plot(x, y2)
plt.title('图表 2')

plt.show()
```

在这里，我们使用`subplot`函数在同一图形中并排创建两个图表。我们向`subplot`传递三个参数：行数、列数和图表编号。然后我们在每个子图中创建一个图表。
