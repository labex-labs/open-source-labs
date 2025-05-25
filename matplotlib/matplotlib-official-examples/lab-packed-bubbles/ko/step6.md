# BubbleChart 객체 생성 및 차트 플롯

패킹된 버블 차트를 생성하려면, `BubbleChart` 객체를 생성하고 `collapse` 메서드를 호출하여 버블을 질량 중심 (center of mass) 으로 이동시켜야 합니다. 그런 다음 `matplotlib` figure 를 생성하고 axes 객체를 추가할 수 있습니다. 마지막으로, `plot` 메서드를 호출하여 차트에 버블을 그립니다.

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
