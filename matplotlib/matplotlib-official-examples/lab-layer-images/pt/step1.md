# Importar as bibliotecas necessárias e definir uma função

Importe as bibliotecas necessárias e defina uma função para criar a primeira imagem.

```python
import matplotlib.pyplot as plt
import numpy as np

def func3(x, y):
    return (1 - x / 2 + x**5 + y**3) * np.exp(-(x**2 + y**2))
```
