# Zeige Linien mit einer angegebenen GID

Der zweite Schritt besteht darin, ein benutzerdefiniertes Tool namens `GroupHideTool` zu erstellen. Die Klasse `GroupHideTool` erbt von `ToolToggleBase`. Die `set_lines_visibility()`-Methode von `GroupHideTool` setzt die Sichtbarkeit aller Linien im Graphen, die die angegebene `GID` haben, je nachdem, ob das Tool aktiviert oder deaktiviert ist, entweder auf `True` oder `False`.

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
