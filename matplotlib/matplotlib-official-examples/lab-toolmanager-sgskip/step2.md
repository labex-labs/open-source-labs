# Show lines with a given gid

The second step is to create a custom tool named `GroupHideTool`. The `GroupHideTool` class inherits from `ToolToggleBase`. The `set_lines_visibility()` method of `GroupHideTool` sets the visibility of all the lines on the plot which have the specified `gid` to either True or False, depending on whether the tool is enabled or disabled.

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
