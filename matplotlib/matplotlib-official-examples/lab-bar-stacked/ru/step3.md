# Создание накопленной столбчатой диаграммы

Мы создадим накопленную столбчатую диаграмму с использованием `matplotlib.pyplot.bar` и пройдемся по каждой категории веса, чтобы накапливать столбцы.

```python
fig, ax = plt.subplots()
bottom = np.zeros(3)

for boolean, weight_count in weight_counts.items():
    p = ax.bar(species, weight_count, width, label=boolean, bottom=bottom)
    bottom += weight_count

ax.set_title("Number of penguins with above average body mass")
ax.legend(loc="upper right")
```
