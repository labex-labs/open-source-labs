# Lidar com Ticks de Data e Hora

Ao trabalhar com valores de data e hora no eixo x, é importante converter as strings em objetos datetime para obter os localizadores e formatadores de data corretos. Aqui está um exemplo:

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

Neste exemplo, convertemos os valores string em datetime64 usando `np.asarray()`. Quando plotamos os dados novamente, os rótulos dos ticks estão como esperado.
