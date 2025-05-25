# Adicionar Texto ao Gráfico

Você pode adicionar texto ao seu gráfico usando a função `ax.text()`. Neste exemplo, adicionaremos texto com diferentes famílias de fontes.

```python
ax.text(0.5, 3., "serif", family="serif")
ax.text(0.5, 2., "monospace", family="monospace")
ax.text(2.5, 2., "sans-serif", family="sans-serif")
ax.set_xlabel(r"µ is not $\mu$")
```
