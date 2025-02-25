# Создаем группированный столбчатый график

Теперь мы можем создать наш график с использованием функции `bar` из Matplotlib. Мы создадим цикл, который будет перебирать наши характеристики и создавать для каждой из них набор столбцов. Также мы настроим ширину столбцов и позицию каждого набора столбцов.

```python
x = np.arange(len(species))
width = 0.25
multiplier = 0

fig, ax = plt.subplots()

for attribute, measurement in penguin_means.items():
    offset = width * multiplier
    rects = ax.bar(x + offset, measurement, width, label=attribute)
    multiplier += 1
```
