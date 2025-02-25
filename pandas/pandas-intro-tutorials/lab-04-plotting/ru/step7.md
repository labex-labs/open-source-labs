# Создаем дополнительные графики для каждого столбца

Мы можем создать отдельные дополнительные графики для каждого столбца данных, используя аргумент subplots.

```python
# Creating subplots for each column
axs = air_quality.plot.area(figsize=(12, 4), subplots=True)
plt.show()
```
