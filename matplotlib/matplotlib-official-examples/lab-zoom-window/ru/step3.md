# Подключение события к функции

Теперь мы подключаем событие нажатия кнопки в первом окне к функции on_press, которую мы только что определили.

```python
figsrc.canvas.mpl_connect('button_press_event', on_press)
```
