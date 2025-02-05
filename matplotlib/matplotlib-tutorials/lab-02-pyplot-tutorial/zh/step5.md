# 自定义线条属性

Matplotlib 允许你自定义各种线条属性，例如线宽、虚线样式和颜色。让我们展示一些设置线条属性的方法：

```python
x = np.arange(0, 5, 0.1)
line, = plt.plot(x, np.sin(x), '-')

# 使用 Line2D 实例的设置方法
line.set_linewidth(2.0)  # 将线条的线宽属性设置为 2.0

# 使用 pyplot.setp 函数
plt.setp(line, color='r', linewidth=2.0)  # 使用 setp 函数设置颜色和线宽属性

plt.show()
```

解释：

- 我们创建一个数组 `x`，并使用 `np.sin` 函数计算相应的 y 值。
- 调用 `plot` 函数创建一个折线图。
- 我们使用 `Line2D` 实例的 `set` 方法将线条的线宽属性设置为 2.0。
- 或者，我们可以使用 `setp` 函数通过关键字参数设置线条的多个属性，如颜色和线宽。
