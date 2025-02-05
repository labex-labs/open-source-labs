# 保存图表

一旦我们创建了一个图表，就可以将其保存到文件中。

```python
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

plt.plot(x, y)
plt.title('我的图表')
plt.xlabel('X轴标签')
plt.ylabel('Y轴标签')
plt.savefig('my_plot.png')
```

在这里，我们使用`savefig`函数将我们的图表保存到一个名为`my_plot.png`的文件中。
