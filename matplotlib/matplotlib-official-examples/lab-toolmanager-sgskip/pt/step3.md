# Adicionar ferramentas personalizadas

O terceiro passo é adicionar as ferramentas personalizadas que criamos nos passos 1 e 2. Isso pode ser alcançado chamando o método `add_tool()` do `ToolManager`. Adicionamos as ferramentas `ListTools` e `GroupHideTool` ao `ToolManager`. Também adicionamos a ferramenta `Show` à `Toolbar`, que foi criada usando o método `add_tool()` da `Toolbar`.

```python
fig.canvas.manager.toolmanager.add_tool('List', ListTools)
fig.canvas.manager.toolmanager.add_tool('Show', GroupHideTool, gid='mygroup')
fig.canvas.manager.toolbar.add_tool('Show', 'navigation', 1)
```
