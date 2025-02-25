# Создание фигуры и осей

Далее мы создадим фигуру и оси с помощью метода `subplots()`. Затем мы построим две линии на оси и добавим легенду, чтобы различить их.

```python
fig, ax = plt.subplots()
ax.plot([1, 2, 3], 'ro-', label='easy as 1 2 3')
ax.plot([1, 4, 9], 'gs--', label='easy as 1 2 3 squared')
ax.legend()
```
