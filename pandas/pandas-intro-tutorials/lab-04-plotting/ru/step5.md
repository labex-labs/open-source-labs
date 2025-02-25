# Создаем точечный график

Для визуального сравнения значений NO2, измеренных в Лондоне и Париже, мы можем создать точечный график.

```python
# Creating a scatter plot
air_quality.plot.scatter(x="station_london", y="station_paris", alpha=0.5)
plt.show()
```
