# Remover Rótulos dos Ticks

Podemos remover os rótulos dos ticks de um subplot específico alterando a visibilidade dos rótulos usando o método `ax.get_xticklabels()`. Neste exemplo, removeremos os rótulos dos ticks no eixo x do segundo subplot.

```python
plt.tick_params('x', labelbottom=False)
```
