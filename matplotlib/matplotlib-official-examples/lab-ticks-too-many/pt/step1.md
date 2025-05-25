# Verifique o Tipo de Dados

O primeiro passo é verificar o tipo de dados dos valores do eixo x. Se for uma lista de strings, é provável que o comportamento dos ticks seja inesperado. Para corrigir isso, precisamos converter as strings em tipos numéricos. Aqui está um exemplo:

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

Neste exemplo, temos uma lista de strings no eixo x. Quando plotamos os dados, os rótulos dos ticks estão fora de ordem e mal posicionados.
