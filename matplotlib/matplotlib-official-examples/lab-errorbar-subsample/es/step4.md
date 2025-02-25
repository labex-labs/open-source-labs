# Desplazar la segunda serie en 3

En algunos casos, es posible que queramos aplicar el submuestreo de barras de error a diferentes partes de nuestros datos. Esto se puede hacer especificando una tupla para el parámetro `errorevery`. Por ejemplo, apliquemos el submuestreo de barras de error a la segunda serie, pero desplacemosla en 3 puntos de datos.

```python
fig, ax = plt.subplots()

ax.set_title('Segunda serie desplazada en 3')
ax.errorbar(x, y1, yerr=y1err, label='y1')
ax.errorbar(x, y2, yerr=y2err, errorevery=(3, 6), label='y2')

ax.legend()
plt.show()
```
