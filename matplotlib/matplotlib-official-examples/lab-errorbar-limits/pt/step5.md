# Adicionar Limites Inferiores

Para adicionar limites inferiores às barras de erro, usaremos o parâmetro `lolims` da função `errorbar`. Também adicionaremos um valor constante de 1.0 aos valores y para diferenciar este gráfico dos anteriores.

```python
# including lower limits
ax.errorbar(x, y + 1.0, xerr=xerr, yerr=yerr, lolims=True, linestyle='dotted')
```
