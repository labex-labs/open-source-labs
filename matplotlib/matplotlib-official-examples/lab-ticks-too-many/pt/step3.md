# Lidar com Muitos Ticks

Se o eixo x tiver muitos elementos, todos os quais são strings, podemos acabar com muitos ticks ilegíveis. Neste caso, precisamos converter as strings em tipos numéricos. Aqui está um exemplo:

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

Neste exemplo, temos 100 valores string no eixo x, resultando em muitos ticks ilegíveis.

Para corrigir isso, precisamos converter as strings em floats. Aqui está um exemplo:

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

Neste exemplo, convertemos os valores string em floats usando `np.asarray()`. Quando plotamos os dados novamente, os rótulos dos ticks estão como esperado.
