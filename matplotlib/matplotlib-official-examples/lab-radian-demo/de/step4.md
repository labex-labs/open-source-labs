# Daten im ersten Teilplot darstellen

Stellen Sie die Kosinuswerte der x-Werte im ersten Teilplot mit der plot-Funktion aus matplotlib.pyplot dar. Verwenden Sie den xunits-Parameter, um anzugeben, dass die x-Achse in Radiant sein soll.

```python
from basic_units import cos
axs[0].plot(x, cos(x), xunits=radians)
```
