# Agregar límites inferiores

Para agregar límites inferiores a las barras de error, usaremos el parámetro `lolims` de la función `errorbar`. También agregaremos un valor constante de 1,0 a los valores de y para diferenciar este gráfico de los anteriores.

```python
# incluyendo límites inferiores
ax.errorbar(x, y + 1.0, xerr=xerr, yerr=yerr, lolims=True, linestyle='dotted')
```
