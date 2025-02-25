# Crear barras de error de theta superpuestas

En este paso, crearemos barras de error de theta superpuestas para demostrar cómo pueden reducir la legibilidad del gráfico de salida.

```python
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(projection='polar')
ax.errorbar(theta, r, xerr=5.25, yerr=0.1, capsize=7, fmt="o", c="darkred")
ax.set_title("Overlapping Theta Error Bars")
plt.show()
```
