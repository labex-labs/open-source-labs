# Afficher les lignes avec un gid donné

La deuxième étape consiste à créer un outil personnalisé nommé `GroupHideTool`. La classe `GroupHideTool` hérite de `ToolToggleBase`. La méthode `set_lines_visibility()` de `GroupHideTool` définit la visibilité de toutes les lignes du tracé qui ont le `gid` spécifié sur True ou False, selon que l'outil est activé ou désactivé.

```python
class GroupHideTool(ToolToggleBase):
    """Afficher les lignes avec un gid donné."""
    default_keymap = 'S'
    description = 'Afficher par gid'
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
