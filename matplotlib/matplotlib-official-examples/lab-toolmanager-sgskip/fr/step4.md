# Supprimer des outils

La quatrième étape consiste à supprimer le bouton `forward` de la `Toolbar`. Nous pouvons le faire en appelant la méthode `remove_tool()` du `ToolManager`.

```python
fig.canvas.manager.toolmanager.remove_tool('forward')
```
