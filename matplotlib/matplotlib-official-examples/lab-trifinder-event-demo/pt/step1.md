# Criar um Objeto de Triangulação

Primeiramente, precisamos criar um objeto `Triangulation`. Usaremos a classe `Triangulation` de `matplotlib.tri`. Neste exemplo, criaremos um objeto `Triangulation` com dados aleatórios.

```python
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.tri import Triangulation

# Generate random data
x = np.random.rand(10)
y = np.random.rand(10)
triang = Triangulation(x, y)
```
