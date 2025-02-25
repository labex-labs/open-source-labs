# Доступ к панели инструментов и VBox

Мы получим доступ к атрибутам панели инструментов и vbox менеджера холста фигуры с использованием методов `manager.toolbar` и `manager.vbox` соответственно.

```python
manager = fig.canvas.manager
toolbar = manager.toolbar
vbox = manager.vbox
```
