# Настройка графика

Мы создаем новый объект фигуры и оси и инициализируем класс `Scope`. Затем мы передаем функции `update` и `emitter` методу `FuncAnimation` для создания анимации.

```python
fig, ax = plt.subplots()
scope = Scope(ax)

ani = animation.FuncAnimation(fig, scope.update, emitter, interval=50,
                              blit=True, save_count=100)

plt.show()
```
