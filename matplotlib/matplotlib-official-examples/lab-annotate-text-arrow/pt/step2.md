# Adicionar anotações de texto ao gráfico

Em seguida, adicionaremos anotações de texto ao gráfico usando a função `ax.text()`. Criaremos duas anotações, uma para "Sample A" (Amostra A) e outra para "Sample B" (Amostra B).

```python
bbox_props = dict(boxstyle="round", fc="w", ec="0.5", alpha=0.9)
ax.text(-2, -2, "Sample A", ha="center", va="center", size=20,
        bbox=bbox_props)
ax.text(2, 2, "Sample B", ha="center", va="center", size=20,
        bbox=bbox_props)
```
