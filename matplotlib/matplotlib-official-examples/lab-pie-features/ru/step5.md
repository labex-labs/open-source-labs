# Настройка цветов

Мы можем настроить цвета секций, передав список цветов в параметр `colors` функции `pie()`.

```python
fig, ax = plt.subplots()
ax.pie(sizes, labels=labels, colors=['olivedrab', 'rosybrown', 'gray','saddlebrown'])
```
