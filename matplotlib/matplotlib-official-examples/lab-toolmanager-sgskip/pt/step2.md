# Mostrar linhas com um determinado gid

O segundo passo é criar uma ferramenta personalizada chamada `GroupHideTool`. A classe `GroupHideTool` herda de `ToolToggleBase`. O método `set_lines_visibility()` de `GroupHideTool` define a visibilidade de todas as linhas no gráfico que possuem o `gid` especificado como True ou False, dependendo se a ferramenta está habilitada ou desabilitada.

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
