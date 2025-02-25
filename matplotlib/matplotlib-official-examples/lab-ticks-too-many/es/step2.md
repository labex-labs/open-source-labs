# Convertir cadenas a tipos numéricos

Para solucionar el comportamiento de las marcas de graduación, necesitamos convertir las cadenas a tipos numéricos. Aquí hay un ejemplo:

```python
import matplotlib.pyplot as plt
import numpy as np

# create example data
x = ['1', '5', '2', '3']
y = [1, 4, 2, 3]

# convert strings to floats
x = np.asarray(x, dtype='float')

# plot the data with numeric tick labels
fig, ax = plt.subplots()
ax.plot(x, y, 'd')
ax.set_xlabel('Floats')
plt.show()
```

En este ejemplo, convertimos los valores de cadena a números de punto flotante usando `np.asarray()`. Cuando representamos los datos nuevamente, las etiquetas de las marcas de graduación son como se esperaba.
