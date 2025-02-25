# Entferne Tools

Der vierte Schritt besteht darin, die Schaltfläche „Vorwärts“ von der `Toolbar` zu entfernen. Wir können dies erreichen, indem wir die `remove_tool()`-Methode des `ToolManager` aufrufen.

```python
fig.canvas.manager.toolmanager.remove_tool('forward')
```
