# 添加自定义工具

第三步是添加我们在步骤 1 和步骤 2 中创建的自定义工具。这可以通过调用 `ToolManager` 的 `add_tool()` 方法来实现。我们将 `ListTools` 和 `GroupHideTool` 工具添加到 `ToolManager` 中。我们还将 `Show` 工具添加到使用 `Toolbar` 的 `add_tool()` 方法创建的 `Toolbar` 中。

```python
fig.canvas.manager.toolmanager.add_tool('List', ListTools)
fig.canvas.manager.toolmanager.add_tool('Show', GroupHideTool, gid='mygroup')
fig.canvas.manager.toolbar.add_tool('Show', 'navigation', 1)
```
