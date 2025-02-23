# Подключаем событие рисования к функции обратного вызова

Нам нужно подключить событие `draw_event` к нашей функции `on_draw`.

```python
fig.canvas.mpl_connect('draw_event', on_draw)
```
