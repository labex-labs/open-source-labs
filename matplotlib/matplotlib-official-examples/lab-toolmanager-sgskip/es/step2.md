# Mostrar líneas con un gid dado

El segundo paso es crear una herramienta personalizada llamada `GroupHideTool`. La clase `GroupHideTool` hereda de `ToolToggleBase`. El método `set_lines_visibility()` de `GroupHideTool` establece la visibilidad de todas las líneas de la gráfica que tienen el `gid` especificado en `True` o `False`, dependiendo de si la herramienta está habilitada o deshabilitada.

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
