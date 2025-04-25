# 置信带

`fill_between` 的一个常见应用是表示置信带。`fill_between` 使用颜色循环中的颜色作为填充颜色。因此，通过使用 `alpha` 使区域半透明来淡化颜色通常是个好做法。

```python
N = 21
x = np.linspace(0, 10, 11)
y = [3.9, 4.4, 10.8, 10.3, 11.2, 13.1, 14.1,  9.9, 13.9, 15.1, 12.5]

# 拟合一条线性曲线并估计其 y 值及其误差。
a, b = np.polyfit(x, y, deg=1)
y_est = a * x + b
y_err = x.std() * np.sqrt(1/len(x) +
                          (x - x.mean())**2 / np.sum((x - x.mean())**2))

fig, ax = plt.subplots()
ax.plot(x, y_est, '-')
ax.fill_between(x, y_est - y_err, y_est + y_err, alpha=0.2)
ax.plot(x, y, 'o', color='tab:brown')
```

在这个示例中：

1. 我们首先定义了数据点的数量 `N`，以及 `x` 和 `y` 数组。
2. 使用 `np.polyfit` 拟合了一条一次多项式曲线（线性曲线），得到系数 `a` 和 `b`，并计算出估计的 `y` 值 `y_est`。
3. 计算了估计值的误差 `y_err`。
4. 创建了一个图形和轴对象，绘制了拟合曲线 `y_est`。
5. 使用 `fill_between` 填充了拟合曲线上下误差范围内的区域，设置 `alpha=0.2` 使填充区域半透明。
6. 最后绘制了原始数据点（用棕色圆点表示）。
