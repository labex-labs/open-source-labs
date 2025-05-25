# Criar o gráfico de barras de erro com subconjuntos de limites superior e inferior

Nesta etapa, criamos um gráfico de barras de erro com subconjuntos de limites superior e inferior.

```python
upperlimits = [True, False] * 5
lowerlimits = [False, True] * 5
plt.errorbar(x, y, yerr=yerr, uplims=upperlimits, lolims=lowerlimits, label='subsets of uplims and lolims')
```
