# Crear un gráfico simple de barras de error

Crearemos un gráfico simple de barras de error con barras de error estándar utilizando la función `errorbar`. Aquí, estableceremos los valores de x e y junto con sus correspondientes valores de error. También estableceremos el estilo de línea en puntos.

```python
fig, ax = plt.subplots(figsize=(7, 4))

# barras de error estándar
ax.errorbar(x, y, xerr=xerr, yerr=yerr, linestyle='dotted')
```
