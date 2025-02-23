# Transformar coordenadas

El siguiente paso es transformar las coordenadas de los datos y la visualización. Usaremos el método `ax.transData` para transformar las coordenadas de los datos y el sistema de coordenadas `píxeles de la figura` para transformar las coordenadas de visualización.

```python
xdata, ydata = 5, 0
xdisplay, ydisplay = ax.transData.transform((xdata, ydata))
```
