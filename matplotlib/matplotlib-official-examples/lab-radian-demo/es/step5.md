# Graficar datos en el segundo subgráfico

Grafica el coseno de los valores de x en el segundo subgráfico utilizando la función plot de matplotlib.pyplot. Utiliza el parámetro xunits para especificar que el eje x debe estar en grados.

```python
from basic_units import degrees
axs[1].plot(x, cos(x), xunits=degrees)
```
