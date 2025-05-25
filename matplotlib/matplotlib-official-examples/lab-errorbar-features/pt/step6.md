# Plotar Escala Logarítmica com Barras de Erro

Finalmente, plotaremos nossos dados com uma escala logarítmica e barras de erro. A função `ax.set_yscale()` é usada para definir o eixo y para uma escala logarítmica.

```python
# plot log scale with error bars
fig, ax = plt.subplots()
ax.errorbar(x, y, yerr=error, fmt='o')
ax.set_title('Log Scale with Error Bars')
ax.set_yscale('log')
plt.show()
```
