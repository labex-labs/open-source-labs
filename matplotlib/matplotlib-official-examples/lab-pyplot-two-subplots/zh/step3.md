# 创建子图

我们将使用 `.pyplot.subplot` 创建一个包含两个子图的图形。

```python
plt.figure()

plt.subplot(211)
plt.plot(t1, f(t1), color='tab:blue', marker='o')
plt.plot(t2, f(t2), color='black')

plt.subplot(212)
plt.plot(t2, np.cos(2*np.pi*t2), color='tab:orange', linestyle='--')

plt.show()
```

`subplot()` 函数接受三个参数：行数、列数和当前子图的索引。索引从左上角的 1 开始，按行增加。在这个例子中，我们创建了一个包含两个子图的图形：一个在上，一个在下。

在第一个子图中，我们绘制 `t1` 与 `f(t1)` 的关系以及 `t2` 与 `f(t2)` 的关系。我们将第一个图的颜色设置为蓝色，并为每个数据点添加圆形标记。我们将第二个图的颜色设置为黑色。

在第二个子图中，我们绘制 `t2` 与 `2*np.pi*t2` 的余弦函数的关系。我们将图的颜色设置为橙色，线型设置为虚线。
