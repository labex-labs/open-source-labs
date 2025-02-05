# Add custom tools

The third step is to add the custom tools that we created in steps 1 and 2. This can be achieved by calling the `add_tool()` method of the `ToolManager`. We add the `ListTools` and `GroupHideTool` tools to the `ToolManager`. We also add the `Show` tool to the `Toolbar`, which was created using the `add_tool()` method of `Toolbar`.

```python
fig.canvas.manager.toolmanager.add_tool('List', ListTools)
fig.canvas.manager.toolmanager.add_tool('Show', GroupHideTool, gid='mygroup')
fig.canvas.manager.toolbar.add_tool('Show', 'navigation', 1)
```
