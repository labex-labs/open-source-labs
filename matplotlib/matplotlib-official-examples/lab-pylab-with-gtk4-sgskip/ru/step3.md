# Доступ к панели инструментов и vbox

```python
manager = fig.canvas.manager
toolbar = manager.toolbar
vbox = manager.vbox
```

Мы получаем доступ к атрибутам `toolbar` и `vbox` менеджера холста фигуры.
