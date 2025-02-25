# Manejar marcas de graduación de fechas y horas

Cuando se trabajan con valores de fechas y horas en el eje x, es importante convertir las cadenas a objetos de fechas y horas para obtener los localizadores y formatos de fecha adecuados. Aquí hay un ejemplo:

```python
import matplotlib.pyplot as plt
import numpy as np

# create example data with datetime strings
x = ['2021-10-01', '2021-11-02', '2021-12-03', '2021-09-01']
y = [0, 2, 3, 1]

# convert strings to datetime64
x = np.asarray(x, dtype='datetime64[s]')

# plot the data with datetime tick labels
fig, ax = plt.subplots()
ax.plot(x, y, 'd')
ax.tick_params(axis='x', labelrotation=90)
plt.show()
```

En este ejemplo, convertimos los valores de cadena a datetime64 usando `np.asarray()`. Cuando representamos los datos nuevamente, las etiquetas de las marcas de graduación son como se esperaba.
