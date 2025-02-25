# Удалить инструменты

Четвёртым шагом является удаление кнопки `forward` из `Toolbar`. Это можно сделать, вызвав метод `remove_tool()` объекта `ToolManager`.

```python
fig.canvas.manager.toolmanager.remove_tool('forward')
```
