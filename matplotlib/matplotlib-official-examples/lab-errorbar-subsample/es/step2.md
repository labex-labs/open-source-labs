# Graficar todas las barras de error

A continuación, graficaremos todas las barras de error utilizando la función `errorbar` sin ningún submuestreo. Esto servirá como nuestra gráfica de referencia.

```python
fig, ax = plt.subplots()

ax.set_title('Todas las barras de error')
ax.errorbar(x, y1, yerr=y1err, label='y1')
ax.errorbar(x, y2, yerr=y2err, label='y2')

ax.legend()
plt.show()
```
