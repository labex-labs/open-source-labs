# Adicionar texto ao gráfico

Adicionaremos texto ao gráfico usando a função `ax.text()`. Adicionaremos texto a quatro locais diferentes no gráfico, cada um com uma família de fontes diferente: serif, monospace, sans-serif e cursive.

```python
ax.text(0.5, 3., "serif")
ax.text(0.5, 2., "monospace", family="monospace")
ax.text(2.5, 2., "sans-serif", family="DejaVu Sans")
ax.text(2.5, 1., "comic", family="cursive")
```
