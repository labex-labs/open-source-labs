# Создаем график

Мы будем использовать функцию `contourf` для создания заполненной карты уровня с логарифмической шкалой цветов:

```python
fig, ax = plt.subplots()
cs = ax.contourf(X, Y, z, locator=ticker.LogLocator(), cmap=cm.PuBu_r)

cbar = fig.colorbar(cs)

plt.show()
```
