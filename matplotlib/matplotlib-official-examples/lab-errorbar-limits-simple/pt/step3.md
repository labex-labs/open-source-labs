# Criar o gráfico de barras de erro com ambos os limites (padrão)

Nesta etapa, criamos um gráfico de barras de erro com limites superior e inferior, que é o comportamento padrão.

```python
plt.errorbar(x, y + 3, yerr=yerr, label='both limits (default)')
```
