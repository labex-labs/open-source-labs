# Importar as bibliotecas necessárias e criar dados

```python
import matplotlib.pyplot as plt
import numpy as np

# Create data
t = np.arange(0.0, 100.0, 0.1)
s = np.sin(0.1 * np.pi * t) * np.exp(-t * 0.01)
```

Primeiramente, importamos as bibliotecas necessárias, ou seja, Matplotlib e NumPy. Em seguida, criamos os dados para plotar. Neste exemplo, criamos um array NumPy "t" e calculamos outro array NumPy "s" usando t.
