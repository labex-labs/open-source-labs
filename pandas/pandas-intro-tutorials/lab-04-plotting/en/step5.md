# Create a Scatter Plot

To visually compare the NO2 values measured in London versus Paris, we can create a scatter plot.

```python
# Creating a scatter plot
air_quality.plot.scatter(x="station_london", y="station_paris", alpha=0.5)
plt.show()
```
