# 特定の gid を持つ線を表示する

2 番目のステップは、`GroupHideTool` という名前のカスタム ツールを作成することです。`GroupHideTool` クラスは `ToolToggleBase` から継承されています。`GroupHideTool` の `set_lines_visibility()` メソッドは、指定された `gid` を持つプロット上のすべての線の表示を、ツールが有効または無効になっているかどうかに応じて True または False に設定します。

```python
class GroupHideTool(ToolToggleBase):
    """Show lines with a given gid."""
    default_keymap = 'S'
    description = 'Show by gid'
    default_toggled = True

    def __init__(self, *args, gid, **kwargs):
        self.gid = gid
        super().__init__(*args, **kwargs)

    def enable(self, *args):
        self.set_lines_visibility(True)

    def disable(self, *args):
        self.set_lines_visibility(False)

    def set_lines_visibility(self, state):
        for ax in self.figure.get_axes():
            for line in ax.get_lines():
                if line.get_gid() == self.gid:
                    line.set_visible(state)
        self.figure.canvas.draw()
```
