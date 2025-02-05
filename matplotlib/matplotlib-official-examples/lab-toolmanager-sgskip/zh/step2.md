# 显示具有给定 gid 的线条

第二步是创建一个名为 `GroupHideTool` 的自定义工具。`GroupHideTool` 类继承自 `ToolToggleBase`。`GroupHideTool` 的 `set_lines_visibility()` 方法根据工具是启用还是禁用，将绘图上所有具有指定 `gid` 的线条的可见性设置为 `True` 或 `False`。

```python
class GroupHideTool(ToolToggleBase):
    """显示具有给定 gid 的线条。"""
    default_keymap = 'S'
    description = '按 gid 显示'
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
