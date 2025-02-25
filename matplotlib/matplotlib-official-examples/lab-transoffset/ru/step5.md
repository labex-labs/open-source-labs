# Создание полярного графика

Теперь мы создадим полярный график с использованием функции `polar` из `matplotlib.pyplot`.

```python
ax = plt.subplot(2, 1, 2, projection='polar')

# Plot the data
for x, y in zip(xs, ys):
    plt.polar(x, y, 'ro')
```
