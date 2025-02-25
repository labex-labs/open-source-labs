# Создаем полярную столбчатую диаграмму

Мы создадим полярную столбчатую диаграмму с использованием параметра `projection='polar'`.

```python
ax = plt.subplot(projection='polar')
ax.bar(theta, radii, width=width, bottom=0.0, color=colors, alpha=0.5)
```
