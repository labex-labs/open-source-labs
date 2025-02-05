# 移除工具

第四步是从工具栏中移除“前进”按钮。我们可以通过调用 `ToolManager` 的 `remove_tool()` 方法来实现这一点。

```python
fig.canvas.manager.toolmanager.remove_tool('forward')
```
