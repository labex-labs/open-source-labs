# Agregar herramientas personalizadas

El tercer paso es agregar las herramientas personalizadas que creamos en los pasos 1 y 2. Esto se puede lograr llamando al método `add_tool()` del `ToolManager`. Agregamos las herramientas `ListTools` y `GroupHideTool` al `ToolManager`. También agregamos la herramienta `Show` a la `Toolbar`, que se creó utilizando el método `add_tool()` de `Toolbar`.

```python
fig.canvas.manager.toolmanager.add_tool('List', ListTools)
fig.canvas.manager.toolmanager.add_tool('Show', GroupHideTool, gid='mygroup')
fig.canvas.manager.toolbar.add_tool('Show', 'navigation', 1)
```
