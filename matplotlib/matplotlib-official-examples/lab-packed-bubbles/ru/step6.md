# Создаем объект BubbleChart и рисуем график

Для создания графика с упакованными пузырьками нам нужно создать объект `BubbleChart` и вызвать метод `collapse`, чтобы переместить пузырьки к центру масс. Затем мы можем создать фигуру `matplotlib` и добавить в нее объект оси. Наконец, мы вызываем метод `plot`, чтобы нарисовать пузырьки на графике.

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
