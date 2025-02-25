# Задаем цвета делений на шкале

Мы задаем цвета делений на шкале для каждой оси y, чтобы они совпадали с цветом меток.

```python
ax.tick_params(axis='y', colors=p1.get_color())
twin1.tick_params(axis='y', colors=p2.get_color())
twin2.tick_params(axis='y', colors=p3.get_color())
```
