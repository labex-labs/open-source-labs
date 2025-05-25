# Adicionar Lenda

Adicionaremos uma legenda ao gráfico usando a função `legend` de `matplotlib.pyplot`. Definiremos as etiquetas para `"não ponderado"` e `"ponderado"`, respectivamente.

```python
plt.legend(
    [disp.surface_.collections[0], wdisp.surface_.collections[0]],
    ["não ponderado", "ponderado"],
    loc="upper right",
)
```
