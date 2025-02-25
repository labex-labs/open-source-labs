# Auflisten aller von `ToolManager` gesteuerten Tools

Der erste Schritt besteht darin, alle von `ToolManager` gesteuerten Tools aufzulisten. Dies kann durch Erstellen eines benutzerdefinierten Tools namens `ListTools` erreicht werden. Die Klasse `ListTools` erbt von `ToolBase`. Die `trigger()`-Methode von `ListTools` druckt den Namen, die Beschreibung und die Tastenkombination aller verfügbaren Tools.

```python
class ListTools(ToolBase):
    """List all the tools controlled by the `ToolManager`."""
    default_keymap = 'm'  # Tastenkombination
    description = 'List Tools'

    def trigger(self, *args, **kwargs):
        print('_' * 80)
        fmt_tool = "{:12} {:45} {}".format
        print(fmt_tool('Name (id)', 'Toolbeschreibung', 'Tastenkombination'))
        print('-' * 80)
        tools = self.toolmanager.tools
        for name in sorted(tools):
            if not tools[name].description:
                continue
            keys = ', '.join(sorted(self.toolmanager.get_tool_keymap(name)))
            print(fmt_tool(name, tools[name].description, keys))
        print('_' * 80)
        fmt_active_toggle = "{!s:12} {!s:45}".format
        print("Aktive Schaltertools")
        print(fmt_active_toggle("Gruppe", "Aktiv"))
        print('-' * 80)
        for group, active in self.toolmanager.active_toggle.items():
            print(fmt_active_toggle(group, active))
```
