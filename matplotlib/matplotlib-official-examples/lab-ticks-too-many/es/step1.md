# Comprueba el tipo de datos

El primer paso es comprobar el tipo de datos de los valores del eje x. Si es una lista de cadenas, es probable que el comportamiento de las marcas de graduación sea inesperado. Para solucionarlo, necesitamos convertir las cadenas a tipos numéricos. Aquí hay un ejemplo:

```python
import matplotlib.pyplot as plt
import numpy as np

# create example data
x = ['1', '5', '2', '3']
y = [1, 4, 2, 3]

# plot the data with string tick labels
fig, ax = plt.subplots()
ax.plot(x, y, 'd')
ax.set_xlabel('Categories')
plt.show()
```

En este ejemplo, tenemos una lista de cadenas en el eje x. Cuando representamos los datos, las etiquetas de las marcas de graduación están desordenadas y mal colocadas.
