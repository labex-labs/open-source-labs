# 创建图表

现在我们已经有了数据，就可以创建图表了。我们将首先使用 `matplotlib.pyplot.subplots()` 创建一个坐标轴对象。然后在这个坐标轴对象上绘制第一组数据，并将标签颜色设置为红色。

```python
fig, ax1 = plt.subplots()

color = 'tab:red'
ax1.set_xlabel('time (s)')
ax1.set_ylabel('exp', color=color)
ax1.plot(t, data1, color=color)
ax1.tick_params(axis='y', labelcolor=color)
```

接下来，我们将使用 `ax1.twinx()` 方法实例化第二个坐标轴对象，它与第一个坐标轴对象共享相同的 x 轴。然后在这个新的坐标轴对象上绘制第二组数据，并将标签颜色设置为蓝色。

```python
ax2 = ax1.twinx()

color = 'tab:blue'
ax2.set_ylabel('sin', color=color)
ax2.plot(t, data2, color=color)
ax2.tick_params(axis='y', labelcolor=color)
```

最后，我们将使用 `fig.tight_layout()` 方法调整图表的布局，并使用 `matplotlib.pyplot.show()` 显示它。

```python
fig.tight_layout()
plt.show()
```
