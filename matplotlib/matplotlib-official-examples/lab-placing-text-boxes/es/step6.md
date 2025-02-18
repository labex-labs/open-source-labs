# Agregar el cuadro de texto al gráfico

Finalmente, agregaremos el cuadro de texto al gráfico utilizando `matplotlib.pyplot.text()`. Especificaremos la ubicación del cuadro de texto en coordenadas de los ejes y utilizaremos el parámetro `bbox` para agregar las propiedades del cuadro.

```python
ax.text(0.05, 0.95, textstr, transform=ax.transAxes, fontsize=14,
        verticalalignment='top', bbox=props)
```
