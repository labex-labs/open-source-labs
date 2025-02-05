# 创建气泡图对象并绘制图表

要创建填充气泡图，我们需要创建一个 `BubbleChart` 对象，并调用 `collapse` 方法将气泡移向质心。然后，我们可以创建一个 `matplotlib` 图形并向其中添加一个坐标轴对象。最后，我们调用 `plot` 方法在图表上绘制气泡。

```python
bubble_chart = BubbleChart(area=browser_market_share['market_share'],
                           bubble_spacing=0.1)

bubble_chart.collapse()

fig, ax = plt.subplots(subplot_kw=dict(aspect="equal"))
bubble_chart.plot(
    ax, browser_market_share['browsers'], browser_market_share['color'])
ax.axis("off")
ax.relim()
ax.autoscale_view()
ax.set_title('Browser market share')

plt.show()
```
