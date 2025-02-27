# Построение кривых обучения для каждого набора данных

Наконец, мы можем построить кривые обучения для каждого набора данных, используя функцию `plot_on_dataset`. Мы создадим сетку графиков размером 2x2 и построим каждый набор данных на отдельной оси.

```python
fig, axes = plt.subplots(2, 2, figsize=(15, 10))

for ax, data, name in zip(
    axes.ravel(), data_sets, ["iris", "digits", "circles", "moons"]
):
    plot_on_dataset(*data, ax=ax, name=name)

fig.legend(ax.get_lines(), labels, ncol=3, loc="upper center")
plt.show()
```
