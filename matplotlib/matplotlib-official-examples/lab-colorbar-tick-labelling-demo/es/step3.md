# Personalizar las etiquetas de los valores de graduación en la barra de color vertical

A continuación, personalizaremos las etiquetas de los valores de graduación en la barra de color vertical. Crearemos una barra de color utilizando `colorbar` y especificaremos las ubicaciones de los valores de graduación utilizando el parámetro `ticks`. Luego estableceremos las etiquetas de los valores de graduación utilizando `set_yticklabels` en el atributo `ax` del objeto de barra de color.

```python
# Add colorbar, make sure to specify tick locations to match desired ticklabels
cbar = fig.colorbar(cax, ticks=[-1, 0, 1])
cbar.ax.set_yticklabels(['< -1', '0', '> 1'])  # vertically oriented colorbar
```
