# Подключение обработчиков событий к полотну фигуры

Теперь мы подключим обработчики событий к полотну фигуры с использованием метода `mpl_connect`. Это позволит вызывать обработчики событий, когда указатель мыши входит в или выходит из фигуры или оси.

```python
fig.canvas.mpl_connect('figure_enter_event', on_enter_figure)
fig.canvas.mpl_connect('figure_leave_event', on_leave_figure)
fig.canvas.mpl_connect('axes_enter_event', on_enter_axes)
fig.canvas.mpl_connect('axes_leave_event', on_leave_axes)
```
