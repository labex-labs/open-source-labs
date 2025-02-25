# Agregar límites superiores e inferiores

Para agregar tanto límites superiores como inferiores a las barras de error, usaremos los parámetros `uplims` y `lolims` de la función `errorbar`. También agregaremos un marcador al gráfico para diferenciarlo de los anteriores.

```python
# incluyendo límites superiores e inferiores
ax.errorbar(x, y + 1.5, xerr=xerr, yerr=yerr, lolims=True, uplims=True,
            marker='o', markersize=8, linestyle='dotted')
```
