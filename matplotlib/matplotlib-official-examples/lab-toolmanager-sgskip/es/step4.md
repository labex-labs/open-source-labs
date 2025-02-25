# Eliminar herramientas

El cuarto paso es eliminar el botón `forward` de la `Toolbar`. Esto se puede lograr llamando al método `remove_tool()` del `ToolManager`.

```python
fig.canvas.manager.toolmanager.remove_tool('forward')
```
