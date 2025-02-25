# Erstellen eines BubbleChart-Objekts und Zeichnen des Diagramms

Um das gepackte Blasen-Diagramm zu erstellen, müssen wir ein `BubbleChart`-Objekt erstellen und die `collapse`-Methode aufrufen, um die Blasen zum Massenmittelpunkt zu bewegen. Anschließend können wir eine `matplotlib`-Figur erstellen und einem Axes-Objekt hinzufügen. Schließlich rufen wir die `plot`-Methode auf, um die Blasen auf dem Diagramm zu zeichnen.

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
