# Создайте график

Создайте объект рисунка и оси с использованием `subplots`. Постройте значения x и y с использованием `plot`. Задайте пределы оси y, чтобы начинаться с 0, с использованием `set_ylim`.

```python
fig, ax = plt.subplots()
ax.plot(x, y, 'r', linewidth=2)
ax.set_ylim(bottom=0)
```
