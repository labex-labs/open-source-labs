# Graficar variable con barras de error simétricas

Ahora graficaremos nuestros datos con barras de error simétricas variables. La función `ax.errorbar()` se utiliza para crear la gráfica, y el parámetro `yerr` se utiliza para especificar los valores de error.

```python
# plot variable, symmetric error bars
fig, ax = plt.subplots()
ax.errorbar(x, y, yerr=error, fmt='-o')
ax.set_title('Variable, Symmetric Error Bars')
plt.show()
```
