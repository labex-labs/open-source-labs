# カスタム ツールを追加する

3 番目のステップは、手順 1 と 2 で作成したカスタム ツールを追加することです。これは、`ToolManager` の `add_tool()` メソッドを呼び出すことで達成できます。`ToolManager` に `ListTools` と `GroupHideTool` のツールを追加します。また、`Toolbar` の `add_tool()` メソッドを使用して作成した `Toolbar` に `Show` ツールも追加します。

```python
fig.canvas.manager.toolmanager.add_tool('List', ListTools)
fig.canvas.manager.toolmanager.add_tool('Show', GroupHideTool, gid='mygroup')
fig.canvas.manager.toolbar.add_tool('Show', 'navigation', 1)
```
