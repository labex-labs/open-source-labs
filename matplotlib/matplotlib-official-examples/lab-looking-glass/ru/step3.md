# Создание фигуры и осей

Мы создадим объект фигуры и оси с использованием функции `subplots()`. Также мы добавим на объект оси круговой участок желтого цвета с использованием функции `patches.Circle()`.

```python
fig, ax = plt.subplots()
circ = patches.Circle((0.5, 0.5), 0.25, alpha=0.8, fc='yellow')
ax.add_patch(circ)
```
