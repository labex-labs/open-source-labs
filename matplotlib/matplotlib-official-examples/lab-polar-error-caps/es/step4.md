# Crear barras de error

En este paso, crearemos barras de error en nuestro eje polar. Utilizaremos la función `errorbar()` para crear barras de error tanto para el radio como para theta.

```python
ax.errorbar(theta, r, xerr=0.25, yerr=0.1, capsize=7, fmt="o", c="seagreen")
```
