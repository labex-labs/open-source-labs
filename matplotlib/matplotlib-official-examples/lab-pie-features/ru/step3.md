# Создание круговой диаграммы

Для создания круговой диаграммы мы будем использовать функцию `pie()` из Matplotlib.

```python
fig, ax = plt.subplots()
ax.pie(sizes, labels=labels)
```
