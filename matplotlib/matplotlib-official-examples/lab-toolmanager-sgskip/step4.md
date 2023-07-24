# Remove tools

The fourth step is to remove the `forward` button from the `Toolbar`. We can achieve this by calling the `remove_tool()` method of the `ToolManager`.

```python
fig.canvas.manager.toolmanager.remove_tool('forward')
```
