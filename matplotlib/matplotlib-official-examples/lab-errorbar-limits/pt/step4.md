# Adicionar Limites Superiores

Para adicionar limites superiores às barras de erro, usaremos o parâmetro `uplims` da função `errorbar`. Também adicionaremos um valor constante de 0.5 aos valores y para diferenciar este gráfico do anterior.

```python
# including upper limits
ax.errorbar(x, y + 0.5, xerr=xerr, yerr=yerr, uplims=True, linestyle='dotted')
```
