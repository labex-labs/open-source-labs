# Adicionando MultiCursor

Finalmente, adicionaremos a função `MultiCursor` para exibir um cursor em todos os três gráficos ao passar o mouse sobre um ponto de dados.

```python
multi = MultiCursor(None, (ax1, ax2, ax3), color='r', lw=1)
plt.show()
```
