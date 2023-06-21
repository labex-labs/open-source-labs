# Create BubbleChart Object and Plot Chart

To create the packed-bubble chart, we need to create a `BubbleChart` object and call the `collapse` method to move the bubbles towards the center of mass. We can then create a `matplotlib` figure and add an axes object to it. Finally, we call the `plot` method to draw the bubbles on the chart.

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
