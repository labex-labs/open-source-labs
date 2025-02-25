# Füge benutzerdefinierte Tools hinzu

Der dritte Schritt besteht darin, die in den Schritten 1 und 2 erstellten benutzerdefinierten Tools hinzuzufügen. Dies kann durch Aufruf der `add_tool()`-Methode des `ToolManager` erreicht werden. Wir fügen die Tools `ListTools` und `GroupHideTool` dem `ToolManager` hinzu. Wir fügen auch das `Show`-Tool der `Toolbar` hinzu, die mit der `add_tool()`-Methode von `Toolbar` erstellt wurde.

```python
fig.canvas.manager.toolmanager.add_tool('List', ListTools)
fig.canvas.manager.toolmanager.add_tool('Show', GroupHideTool, gid='mygroup')
fig.canvas.manager.toolbar.add_tool('Show', 'navigation', 1)
```
