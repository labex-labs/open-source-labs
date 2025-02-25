# Crear barras de error de radio grandes

En este paso, crearemos barras de error de radio grandes para demostrar cómo pueden causar una escala no deseada en los datos, reduciendo el rango mostrado.

```python
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(projection='polar')
ax.errorbar(theta, r, xerr=0.25, yerr=10.1, capsize=7, fmt="o", c="orangered")
ax.set_title("Large Radius Error Bars")
plt.show()
```
