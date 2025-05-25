# Converter Strings para Tipos Numéricos

Para corrigir o comportamento dos ticks, precisamos converter as strings em tipos numéricos. Aqui está um exemplo:

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

Neste exemplo, convertemos os valores string em floats usando `np.asarray()`. Quando plotamos os dados novamente, os rótulos dos ticks estão como esperado.
