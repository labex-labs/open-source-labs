# Erstellen eines Punktdiagramms

Um die gemessenen NO2-Werte in London und Paris visuell zu vergleichen, können wir ein Punktdiagramm erstellen.

```python
# Creating a scatter plot
air_quality.plot.scatter(x="station_london", y="station_paris", alpha=0.5)
plt.show()
```
