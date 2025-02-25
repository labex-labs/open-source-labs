# ツールを削除する

4 番目のステップは、`Toolbar` から `forward` ボタンを削除することです。これは、`ToolManager` の `remove_tool()` メソッドを呼び出すことで達成できます。

```python
fig.canvas.manager.toolmanager.remove_tool('forward')
```
