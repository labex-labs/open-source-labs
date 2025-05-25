# Listar todas as ferramentas controladas pelo `ToolManager`

O primeiro passo é listar todas as ferramentas controladas pelo `ToolManager`. Isso pode ser alcançado criando uma ferramenta personalizada chamada `ListTools`. A classe `ListTools` herda de `ToolBase`. O método `trigger()` de `ListTools` imprime o nome, a descrição e o keymap (mapa de teclas) de todas as ferramentas disponíveis.

```python
class ListTools(ToolBase):
    """List all the tools controlled by the `ToolManager`."""
    default_keymap = 'm'  # keyboard shortcut
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
