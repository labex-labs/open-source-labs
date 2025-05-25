# 사용자 정의 도구 추가

세 번째 단계는 1 단계와 2 단계에서 생성한 사용자 정의 도구를 추가하는 것입니다. 이는 `ToolManager`의 `add_tool()` 메서드를 호출하여 수행할 수 있습니다. `ListTools` 및 `GroupHideTool` 도구를 `ToolManager`에 추가합니다. 또한 `Toolbar`의 `add_tool()` 메서드를 사용하여 생성된 `Show` 도구를 `Toolbar`에 추가합니다.

```python
fig.canvas.manager.toolmanager.add_tool('List', ListTools)
fig.canvas.manager.toolmanager.add_tool('Show', GroupHideTool, gid='mygroup')
fig.canvas.manager.toolbar.add_tool('Show', 'navigation', 1)
```
