# Manejar demasiadas marcas de graduación

Si el eje x tiene muchos elementos, todos ellos cadenas, es posible que terminemos con demasiadas marcas de graduación que son ilegibles. En este caso, necesitamos convertir las cadenas a tipos numéricos. Aquí hay un ejemplo:

```python
import matplotlib.pyplot as plt
import numpy as np

# create example data with 100 elements
x = [f'{xx}' for xx in np.arange(100)]
y = np.arange(100)

# plot the data with string tick labels
fig, ax = plt.subplots()
ax.plot(x, y)
ax.set_xlabel('Categories')
plt.show()
```

En este ejemplo, tenemos 100 valores de cadena en el eje x, lo que resulta en demasiadas marcas de graduación que son ilegibles.

Para solucionarlo, necesitamos convertir las cadenas a números de punto flotante. Aquí hay un ejemplo:

```python
import matplotlib.pyplot as plt
import numpy as np

# create example data with 100 elements
x = [f'{xx}' for xx in np.arange(100)]
y = np.arange(100)

# convert strings to floats
x = np.asarray(x, float)

# plot the data with numeric tick labels
fig, ax = plt.subplots()
ax.plot(x, y)
ax.set_xlabel('Floats')
plt.show()
```

En este ejemplo, convertimos los valores de cadena a números de punto flotante usando `np.asarray()`. Cuando representamos los datos nuevamente, las etiquetas de las marcas de graduación son como se esperaba.
