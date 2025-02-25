# Показать линии с заданным gid

Вторым шагом является создание пользовательского инструмента под названием `GroupHideTool`. Класс `GroupHideTool` наследуется от `ToolToggleBase`. Метод `set_lines_visibility()` класса `GroupHideTool` назначает видимость всех линий на графике, имеющих указанный `gid`, либо `True`, либо `False`, в зависимости от того, включен ли инструмент или нет.

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
