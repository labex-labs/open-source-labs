# Создаем график и подключаем событие прокрутки

Мы создадим график с использованием функции `subplots` из Matplotlib и передадим созданный объект `IndexTracker` в него. Затем мы подключим событие прокрутки к полотну фигуры с использованием `mpl_connect`.

```python
fig, ax = plt.subplots()
tracker = IndexTracker(ax, X)

fig.canvas.mpl_connect('scroll_event', tracker.on_scroll)
plt.show()
```
