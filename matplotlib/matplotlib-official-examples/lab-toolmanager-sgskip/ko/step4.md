# 도구 제거

네 번째 단계는 `Toolbar`에서 `forward` 버튼을 제거하는 것입니다. 이는 `ToolManager`의 `remove_tool()` 메서드를 호출하여 수행할 수 있습니다.

```python
fig.canvas.manager.toolmanager.remove_tool('forward')
```
