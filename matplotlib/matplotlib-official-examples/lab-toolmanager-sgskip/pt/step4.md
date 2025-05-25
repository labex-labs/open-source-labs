# Remover ferramentas

O quarto passo é remover o botão `forward` da `Toolbar`. Podemos conseguir isso chamando o método `remove_tool()` do `ToolManager`.

```python
fig.canvas.manager.toolmanager.remove_tool('forward')
```
