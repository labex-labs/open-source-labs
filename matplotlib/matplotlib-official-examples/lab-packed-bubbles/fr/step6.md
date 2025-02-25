# Créer un objet BubbleChart et tracer le graphique

Pour créer le graphique à bulles empaquetées, nous devons créer un objet `BubbleChart` et appeler la méthode `collapse` pour déplacer les bulles vers le centre de masse. Nous pouvons ensuite créer une figure `matplotlib` et y ajouter un objet d'axes. Enfin, nous appelons la méthode `plot` pour tracer les bulles sur le graphique.

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
