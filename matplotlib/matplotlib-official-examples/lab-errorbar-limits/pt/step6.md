# Adicionar Limites Superiores e Inferiores

Para adicionar limites superiores e inferiores às barras de erro, usaremos os parâmetros `uplims` e `lolims` da função `errorbar`. Também adicionaremos um marcador ao gráfico para diferenciá-lo dos anteriores.

```python
# including upper and lower limits
ax.errorbar(x, y + 1.5, xerr=xerr, yerr=yerr, lolims=True, uplims=True,
            marker='o', markersize=8, linestyle='dotted')
```
