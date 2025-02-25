# Добавить пользовательские инструменты

Третий шаг - добавить пользовательские инструменты, созданные нами на шагах 1 и 2. Это можно сделать, вызвав метод `add_tool()` объекта `ToolManager`. Мы добавляем инструменты `ListTools` и `GroupHideTool` в `ToolManager`. Также добавляем инструмент `Show` в `Toolbar`, который был создан с использованием метода `add_tool()` объекта `Toolbar`.

```python
fig.canvas.manager.toolmanager.add_tool('List', ListTools)
fig.canvas.manager.toolmanager.add_tool('Show', GroupHideTool, gid='mygroup')
fig.canvas.manager.toolbar.add_tool('Show', 'navigation', 1)
```
