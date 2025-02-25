# Graficar datos en el primer subgráfico

Grafica el coseno de los valores de x en el primer subgráfico utilizando la función plot de matplotlib.pyplot. Utiliza el parámetro xunits para especificar que el eje x debe estar en radianes.

```python
from basic_units import cos
axs[0].plot(x, cos(x), xunits=radians)
```
