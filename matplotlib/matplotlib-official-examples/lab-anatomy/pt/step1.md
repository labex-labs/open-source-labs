# Importar bibliotecas e configurar dados

Primeiramente, precisamos importar as bibliotecas necessárias e configurar alguns dados para plotar. Neste exemplo, plotaremos três ondas senoidais com algum ruído aleatório adicionado a elas.

```python
import matplotlib.pyplot as plt
import numpy as np

# Set up data
np.random.seed(19680801)

X = np.linspace(0.5, 3.5, 100)
Y1 = 3+np.cos(X)
Y2 = 1+np.cos(1+X/0.75)/2
Y3 = np.random.uniform(Y1, Y2, len(X))
```
