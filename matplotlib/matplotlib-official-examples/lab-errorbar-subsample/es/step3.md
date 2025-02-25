# Submuestrear cada sexta barra de error

Ahora, aplicaremos el submuestreo de barras de error para graficar solo cada sexta barra de error. Esto se puede hacer utilizando el parámetro `errorevery` de la función `errorbar`.

```python
fig, ax = plt.subplots()

ax.set_title('Cada sexta barra de error')
ax.errorbar(x, y1, yerr=y1err, errorevery=6, label='y1')
ax.errorbar(x, y2, yerr=y2err, errorevery=6, label='y2')

ax.legend()
plt.show()
```
