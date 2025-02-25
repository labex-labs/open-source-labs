# Agregar límites superiores

Para agregar límites superiores a las barras de error, usaremos el parámetro `uplims` de la función `errorbar`. También agregaremos un valor constante de 0,5 a los valores de y para diferenciar este gráfico del anterior.

```python
# incluyendo límites superiores
ax.errorbar(x, y + 0.5, xerr=xerr, yerr=yerr, uplims=True, linestyle='dotted')
```
