# Lister tous les outils contrôlés par le `ToolManager`

La première étape consiste à lister tous les outils contrôlés par le `ToolManager`. Cela peut être réalisé en créant un outil personnalisé nommé `ListTools`. La classe `ListTools` hérite de `ToolBase`. La méthode `trigger()` de `ListTools` affiche le nom, la description et la carte de touches de tous les outils disponibles.

```python
class ListTools(ToolBase):
    """Lister tous les outils contrôlés par le `ToolManager`."""
    default_keymap = 'm'  # raccourci clavier
    description = 'Lister les outils'

    def trigger(self, *args, **kwargs):
        print('_' * 80)
        fmt_tool = "{:12} {:45} {}".format
        print(fmt_tool('Nom (id)', 'Description de l\'outil', 'Carte de touches'))
        print('-' * 80)
        tools = self.toolmanager.tools
        for name in sorted(tools):
            if not tools[name].description:
                continue
            keys = ', '.join(sorted(self.toolmanager.get_tool_keymap(name)))
            print(fmt_tool(name, tools[name].description, keys))
        print('_' * 80)
        fmt_active_toggle = "{!s:12} {!s:45}".format
        print("Activer/Désactiver les outils")
        print(fmt_active_toggle("Groupe", "Actif"))
        print('-' * 80)
        for group, active in self.toolmanager.active_toggle.items():
            print(fmt_active_toggle(group, active))
```
