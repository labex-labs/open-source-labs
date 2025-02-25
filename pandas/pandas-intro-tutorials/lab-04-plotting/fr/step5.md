# Créer un graphique en nuage de points

Pour comparer visuellement les valeurs de NO2 mesurées à Londres et à Paris, nous pouvons créer un graphique en nuage de points.

```python
# Creating a scatter plot
air_quality.plot.scatter(x="station_london", y="station_paris", alpha=0.5)
plt.show()
```
