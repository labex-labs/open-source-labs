# Перечислить все инструменты, контролируемые `ToolManager`

Первым шагом является перечисление всех инструментов, контролируемых `ToolManager`. Это можно сделать, создав пользовательский инструмент под названием `ListTools`. Класс `ListTools` наследуется от `ToolBase`. Метод `trigger()` класса `ListTools` выводит имя, описание и клавишу для всех доступных инструментов.

```python
class ListTools(ToolBase):
    """List all the tools controlled by the `ToolManager`."""
    default_keymap = 'm'  # сочетание клавиш для быстрого доступа
    description = 'List Tools'

    def trigger(self, *args, **kwargs):
        print('_' * 80)
        fmt_tool = "{:12} {:45} {}".format
        print(fmt_tool('Name (id)', 'Tool description', 'Keymap'))
        print('-' * 80)
        tools = self.toolmanager.tools
        for name in sorted(tools):
            if not tools[name].description:
                continue
            keys = ', '.join(sorted(self.toolmanager.get_tool_keymap(name)))
            print(fmt_tool(name, tools[name].description, keys))
        print('_' * 80)
        fmt_active_toggle = "{!s:12} {!s:45}".format
        print("Active Toggle tools")
        print(fmt_active_toggle("Group", "Active"))
        print('-' * 80)
        for group, active in self.toolmanager.active_toggle.items():
            print(fmt_active_toggle(group, active))
```
