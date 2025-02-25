# Daten im zweiten Teilplot darstellen

Stellen Sie die Kosinuswerte der x-Werte im zweiten Teilplot mit der plot-Funktion aus matplotlib.pyplot dar. Verwenden Sie den xunits-Parameter, um anzugeben, dass die x-Achse in Grad sein soll.

```python
from basic_units import degrees
axs[1].plot(x, cos(x), xunits=degrees)
```
