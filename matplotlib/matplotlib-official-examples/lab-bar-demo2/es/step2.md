# Crear datos para el gráfico de barras

En este paso, necesitamos crear datos para el gráfico de barras. Utilizaremos la biblioteca numpy para crear una matriz de valores que utilizaremos para el gráfico de barras.

```python
from basic_units import cm, inch

cms = cm * np.arange(0, 10, 2)
bottom = 0 * cm
width = 0.8 * cm
```
