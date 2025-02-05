# 创建斜 T - 对数 P 图

现在我们将使用之前注册的 SkewXAxes 投影来创建斜 T - 对数 P 图。我们首先创建一个图形对象，并添加一个具有 SkewXAxes 投影的子图。然后，我们将使用 semilogy 函数在图上绘制温度和露点数据。最后，我们将设置 X 轴和 Y 轴的范围和刻度，并显示该图。

```python
fig = plt.figure(figsize=(6.5875, 6.2125))
ax = fig.add_subplot(projection='skewx')

ax.semilogy(T, p, color='C3')
ax.semilogy(Td, p, color='C2')

ax.axvline(0, color='C0')

ax.yaxis.set_major_formatter(ScalarFormatter())
ax.yaxis.set_minor_formatter(NullFormatter())
ax.set_yticks(np.linspace(100, 1000, 10))
ax.set_ylim(1050, 100)

ax.xaxis.set_major_locator(MultipleLocator(10))
ax.set_xlim(-50, 50)

plt.grid(True)
plt.show()
```
