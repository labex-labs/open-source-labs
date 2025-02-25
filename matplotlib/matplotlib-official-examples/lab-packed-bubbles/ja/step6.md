# BubbleChart オブジェクトを作成してチャートを描画する

パックドバブルチャートを作成するには、`BubbleChart` オブジェクトを作成し、`collapse` メソッドを呼び出してバブルを質量中心に向かって移動させます。その後、`matplotlib` のグラフを作成し、そこに軸オブジェクトを追加します。最後に、`plot` メソッドを呼び出してチャート上にバブルを描画します。

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
