# Подключение обработчиков событий

Мы подключим обработчики событий к холсту фигуры.

```python
browser = PointBrowser()

fig.canvas.mpl_connect('pick_event', browser.on_pick)
fig.canvas.mpl_connect('key_press_event', browser.on_press)
```
