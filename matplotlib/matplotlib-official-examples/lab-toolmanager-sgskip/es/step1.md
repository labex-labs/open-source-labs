# Lista todas las herramientas controladas por el `ToolManager`

El primer paso es listar todas las herramientas controladas por el `ToolManager`. Esto se puede lograr creando una herramienta personalizada llamada `ListTools`. La clase `ListTools` hereda de `ToolBase`. El método `trigger()` de `ListTools` imprime el nombre, la descripción y el mapeo de teclas de todas las herramientas disponibles.

```python
class ListTools(ToolBase):
    """List all the tools controlled by the `ToolManager`."""
    default_keymap = 'm'  # atajo de teclado
    description = 'List Tools'

    def trigger(self, *args, **kwargs):
        print('_' * 80)
        fmt_tool = "{:12} {:45} {}".format
        print(fmt_tool('Nombre (id)', 'Descripción de la herramienta', 'Mapeo de teclas'))
        print('-' * 80)
        tools = self.toolmanager.tools
        for name in sorted(tools):
            if not tools[name].description:
                continue
            keys = ', '.join(sorted(self.toolmanager.get_tool_keymap(name)))
            print(fmt_tool(name, tools[name].description, keys))
        print('_' * 80)
        fmt_active_toggle = "{!s:12} {!s:45}".format
        print("Herramientas de conmutación activa")
        print(fmt_active_toggle("Grupo", "Activo"))
        print('-' * 80)
        for group, active in self.toolmanager.active_toggle.items():
            print(fmt_active_toggle(group, active))
```
