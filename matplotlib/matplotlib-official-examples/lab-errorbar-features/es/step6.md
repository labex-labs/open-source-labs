# Graficar en escala logarítmica con barras de error

Finalmente, graficaremos nuestros datos en una escala logarítmica con barras de error. La función `ax.set_yscale()` se utiliza para establecer el eje y en una escala logarítmica.

```python
# plot log scale with error bars
fig, ax = plt.subplots()
ax.errorbar(x, y, yerr=error, fmt='o')
ax.set_title('Log Scale with Error Bars')
ax.set_yscale('log')
plt.show()
```
