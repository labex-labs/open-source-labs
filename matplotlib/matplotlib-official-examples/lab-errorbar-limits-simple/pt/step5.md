# Criar o gráfico de barras de erro com limites superior e inferior

Nesta etapa, criamos um gráfico de barras de erro com limites superior e inferior.

```python
plt.errorbar(x, y + 1, yerr=yerr, uplims=True, lolims=True, label='uplims=True, lolims=True')
```
