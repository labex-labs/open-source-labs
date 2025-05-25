# Criar o gráfico de barras de erro apenas com limites superiores

Nesta etapa, criamos um gráfico de barras de erro com apenas limites superiores.

```python
plt.errorbar(x, y + 2, yerr=yerr, uplims=True, label='uplims=True')
```
