# Ajouter des outils personnalisés

La troisième étape consiste à ajouter les outils personnalisés que nous avons créés dans les étapes 1 et 2. Cela peut être réalisé en appelant la méthode `add_tool()` du `ToolManager`. Nous ajoutons les outils `ListTools` et `GroupHideTool` au `ToolManager`. Nous ajoutons également l'outil `Show` à la `Toolbar`, qui a été créée à l'aide de la méthode `add_tool()` de `Toolbar`.

```python
fig.canvas.manager.toolmanager.add_tool('List', ListTools)
fig.canvas.manager.toolmanager.add_tool('Show', GroupHideTool, gid='mygroup')
fig.canvas.manager.toolbar.add_tool('Show', 'navigation', 1)
```
